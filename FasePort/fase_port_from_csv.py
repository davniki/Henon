import matplotlib.pyplot as plt
import pandas as pd
import os
import re
import tkinter as tk
from tkinter import filedialog


# --- ЗАГРУЗКА ---
def load_csv(filepath):
    """Загружает CSV, пропуская строки-комментарии."""
    return pd.read_csv(filepath, comment='#')


def parse_params_from_filename(filename):
    """
    Пытается извлечь параметры из имени файла.
    Пример: phase_zoom2_a1p430_b0p5_cm1p7594_dps24_k10000.csv
    """
    pattern = (
        r'(?P<name>phase_\w+?)'
        r'_a(?P<a>[\dmp]+)'
        r'_b(?P<b>[\dmp]+)'
        r'_c(?P<c>[\dmp]+)'
        r'_dps(?P<dps>\d+)'
        r'(?:_(?P<count_label>[nMkl])(?P<count>\d+))?'
    )
    m = re.search(pattern, filename)
    if not m:
        return None
    d = m.groupdict()

    def to_float(s):
        return float(s.replace('p', '.').replace('m', '-'))

    return {
        'name': d['name'],
        'a': to_float(d['a']),
        'b': to_float(d['b']),
        'c': to_float(d['c']),
        'dps': int(d['dps']),
        'count': int(d['count']) if d['count'] else None,
        'count_label': d['count_label'],
    }


# --- ДИАЛОГ ВЫБОРА ФАЙЛОВ ---
root = tk.Tk()
root.withdraw()

input_dir = 'Portraits'
if not os.path.isdir(input_dir):
    input_dir = os.getcwd()

print("📂 Выберите CSV-файлы для построения...")

filepaths = filedialog.askopenfilenames(
    title="Выберите CSV-файлы с фазовыми портретами",
    initialdir=os.path.abspath(input_dir),
    filetypes=[("CSV files", "*.csv"), ("All files", "*.*")]
)

if not filepaths:
    print("❌ Файлы не выбраны. Выход.")
    exit()

print(f"✅ Выбрано файлов: {len(filepaths)}\n")

# --- НАСТРОЙКИ КАЧЕСТВА ---
plt.rcParams['figure.dpi'] = 300
plt.rcParams['savefig.dpi'] = 600
plt.rcParams['font.size'] = 12

output_dir = 'Portraits/Pictures'
os.makedirs(output_dir, exist_ok=True)

# --- ОТРИСОВКА КАЖДОГО ВЫБРАННОГО ФАЙЛА ---
for filepath in filepaths:
    filename = os.path.basename(filepath)
    print(f"📊 Обработка: {filename}")

    df = load_csv(filepath)
    if df.empty:
        print(f"   ⚠️ Файл пуст, пропускаем")
        continue

    # Пытаемся извлечь параметры из имени
    info = parse_params_from_filename(filename)

    if info:
        title = (
            # f"{info['name']} | "
            f"a={info['a']}, b={info['b']}, c={info['c']} | "
            f"dps={info['dps']} | "
            f"точек={info['count']}"
        )
    else:
        title = filename

    fig, ax = plt.subplots()

    ax.plot(
        df['x'], df['y'],
        linestyle='none',
        marker='.',
        markersize=0.99,
        markeredgewidth=0,
        alpha=1.0,
        color='green',
        rasterized=True,
    )

    ax.set_title(title, fontsize=10)
    ax.grid(alpha=0.3)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')

    # Имя выходного файла — на основе входного
    out_name = os.path.splitext(filename)[0] + '.png'
    out_path = os.path.join(output_dir, out_name)

    plt.savefig(out_path, dpi=600, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    print(f"   ✅ Сохранён: {out_path}")
    plt.close()

print("\n🎉 Готово!")