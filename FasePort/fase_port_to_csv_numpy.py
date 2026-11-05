# fase_port_to_csv_numpy.py
import numpy as np
from sys import stdout
from models_numpy import henon   # ← numpy-версия
import os
import csv


# --- ПАРАМЕТРЫ ---
a = np.float64(1.43)
b = np.float64(0.5)
c = np.float64(-1.7594137)

# --- НАЧАЛЬНЫЕ УСЛОВИЯ ---
x = np.array([0.1, 0.1, 0.1], dtype=np.float64)

# --- СПИСКИ ДЛЯ ДАННЫХ ---
fase_port_1 = []
fase_port_2 = []

# --- ТРАНЗИЕНТ ---
print("Транзиент...")
for i in range(1_000_000):
    x = henon(x, a, b, c)

# --- ОСНОВНОЙ ЦИКЛ ---
n = M = k = 0

while k != 10_000:
    stdout.write("\r%d" % k)
    stdout.flush()

    x = henon(x, a, b, c)
    n += 1

    if (-0.38 < x[0] < -0.36) and (-0.414 < x[1] < -0.405):
        fase_port_1.append((x[0], x[1], x[2]))
        M += 1

    if (-0.381 < x[0] < -0.378) and (-0.4088 < x[1] < -0.408):
        fase_port_2.append((x[0], x[1], x[2]))
        k += 1

print('\n', n, M, k, sep='\n')

# --- СОХРАНЕНИЕ В CSV ---
output_dir = 'Portraits/CSV'
os.makedirs(output_dir, exist_ok=True)
print(f"📁 Данные будут сохранены в: {os.path.abspath(output_dir)}")


def safe_num(val):
    s = str(val)
    return s.replace('.', 'p').replace('-', 'm').replace('+', '')


params_str = (
    f"a{safe_num(a)}"
    f"_b{safe_num(b)}"
    f"_c{safe_num(c)}"
    f"_dps16"      # float64 ≈ 16 значащих цифр
    f"_f64"        # маркер numpy
)


def save_to_csv(data, filepath, params=None):
    with open(filepath, 'w', newline='') as f:
        if params:
            for key, val in params.items():
                f.write(f"# {key} = {val}\n")
        f.write("x,y,z\n")
        writer = csv.writer(f)
        for xi, yi, zi in data:
            writer.writerow([float(xi), float(yi), float(zi)])


params = {
    'a': a, 'b': b, 'c': c,
    'dtype': 'float64',
    'machine_eps': np.finfo(np.float64).eps,
}

files = [
    (fase_port_1, f"phase_zoom1_{params_str}_M{len(fase_port_1)}_np.csv"),
    (fase_port_2, f"phase_zoom2_{params_str}_k{len(fase_port_2)}_np.csv"),
]

for data, filename in files:
    if not data:
        print(f"⚠️ Пропускаем пустой набор: {filename}")
        continue
    filepath = os.path.join(output_dir, filename)
    save_to_csv(data, filepath, params)
    print(f"✅ Сохранён: {filename} ({len(data)} точек)")

print(f"\n🎉 Все CSV сохранены в: {os.path.abspath(output_dir)}")