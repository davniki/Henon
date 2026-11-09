import matplotlib.pyplot as plt
from sys import stdout
from models import henon, henon_noisy
from mpmath import mp
import os
import csv
import random

mp.dps = 24

###
#  Фазовый портрет динамической системы с аддитивным белым гауссовым шумом (AWGN)
###

a = mp.mpf('1.43')
b = mp.mpf('0.5')
c = mp.mpf('-1.7594137')

# === Параметры шума и воспроизводимости ===
sigma = mp.mpf('1e-20')
seed  = 42
random.seed(seed)        # mp.rand() = random.random(), поэтому влияет и на _gauss()

x = [mp.mpf('0.1'), mp.mpf('0.1'), mp.mpf('0.1')]

fase_port_0 = []  # полный портрет
fase_port_1 = []  # увеличение 1
fase_port_2 = []  # увеличение 2

# === Переходный процесс (без шума) ===
print("Переходный процесс...")
for i in range(1_000_000):
    x = henon(x, a, b, c)

# === Основной цикл (с шумом) ===
n = M = k = 0
max_iter = 50_000_000
append_every = 1
it = 0

while k != 10_000:
    # it += 1
    # if it > max_iter:
    #     print(f"\n⚠️  Предохранитель: it={it}, k={k}, M={M}, n={n}. "
    #           f"Уменьшите sigma, увеличьте mp.dps или расширьте окна.")
    #     break

    stdout.write("\r%d" % k)
    stdout.flush()

    x = henon_noisy(x, a, b, c, sigma)

    # if n % append_every == 0:
    #   fase_port_0.append((x[0], x[1], x[2]))
    n += 1

    if (-0.38 < x[0] < -0.36) and (-0.414 < x[1] < -0.405):
        fase_port_1.append((x[0], x[1], x[2]))
        M += 1

    if (-0.381 < x[0] < -0.378) and (-0.4088 < x[1] < -0.408):
        fase_port_2.append((x[0], x[1], x[2]))
        k += 1

print('\n', n, M, k, sep='\n')

# --- СОХРАНЕНИЕ В CSV ---

output_dir = 'Portraits_awgn'
os.makedirs(output_dir, exist_ok=True)
print(f"📁 Данные будут сохранены в: {os.path.abspath(output_dir)}")

# Заменяем точки и минусы, чтобы имя было безопасным для файловой системы
def safe_num(val):
    """Форматирует число: '.' -> 'p', '-' -> 'm', '+' убираем."""
    s = str(val)
    return s.replace('.', 'p').replace('-', 'm').replace('+', '')

# Общая часть имени: a, b, c, dps, sigma, seed + метка AWGN
params_str = (
    f"a{safe_num(a)}"
    f"_b{safe_num(b)}"
    f"_c{safe_num(c)}"
    f"_dps{mp.dps}"
    f"_sig{safe_num(sigma)}"
    f"_seed{seed}"
    f"_awgn"
)

def save_to_csv(data, filepath, params=None):
    """Сохраняет список кортежей (x, y, z) в CSV. params — шапка-комментарий."""
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
    'mp.dps': mp.dps,
    # 'mpmath_version': mp.__version__,
    'noise': 'AWGN',
    'sigma': sigma,
    'seed': seed,
    'model': 'henon_noisy (additive, right-hand side, all 3 equations)',
    'append_every': append_every,
}

# Имена файлов — как в fase_port_to_csv.py + суффикс _awgn в params_str
files = [
    # (fase_port_0, f"phase_full_{params_str}_n{len(fase_port_0)}.csv"),
    (fase_port_1, f"phase_zoom1_{params_str}_M{len(fase_port_1)}.csv"),
    (fase_port_2, f"phase_zoom2_{params_str}_k{len(fase_port_2)}.csv"),
]

for data, filename in files:
    if not data:
        print(f"⚠️ Пропускаем пустой набор: {filename}")
        continue
    filepath = os.path.join(output_dir, filename)
    save_to_csv(data, filepath, params)
    print(f"✅ Сохранён: {filename} ({len(data)} точек)")

print(f"\n🎉 Все CSV сохранены в: {os.path.abspath(output_dir)}")