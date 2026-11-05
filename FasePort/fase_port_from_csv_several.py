import matplotlib.pyplot as plt
import pandas as pd
import os
import re
import tkinter as tk
from tkinter import filedialog


# ============================================================
#  ЗАМЕНА simpledialog.askstring (обходит ошибку MacWindowStyle)
# ============================================================
def ask_string_custom(title, prompt, initialvalue=""):
    """Кастомный диалог ввода строки, работает на macOS с Tk 9.x."""
    result = {"value": None}

    win = tk.Toplevel()
    win.title(title)
    win.geometry("550x200")
    win.resizable(False, False)

    tk.Label(win, text=prompt, wraplength=500,
             justify='left').pack(pady=(12, 6), padx=12, anchor='w')

    entry = tk.Entry(win, width=65)
    entry.insert(0, initialvalue)
    entry.pack(pady=6, padx=12, fill='x')
    entry.select_range(0, 'end')
    entry.focus_set()

    def on_ok():
        result["value"] = entry.get()
        win.destroy()

    def on_cancel():
        win.destroy()

    entry.bind('<Return>', lambda e: on_ok())
    win.bind('<Escape>', lambda e: on_cancel())

    btn_frame = tk.Frame(win)
    btn_frame.pack(pady=12)
    tk.Button(btn_frame, text="OK", width=12,
              command=on_ok).pack(side='left', padx=6)
    tk.Button(btn_frame, text="Cancel", width=12,
              command=on_cancel).pack(side='left', padx=6)

    win.transient()
    win.grab_set()
    win.wait_window()

    return result["value"]


# ============================================================
#  ЗАГРУЗКА
# ============================================================
def load_csv(filepath):
    """Загружает CSV, пропуская строки-комментарии."""
    return pd.read_csv(filepath, comment='#')


def parse_params_from_filename(filename):
    """Извлекает параметры из имени файла."""
    pattern = (
        r'(?P<name>phase_\w+?)'
        r'_a(?P<a>[\dmp]+)'
        r'_b(?P<b>[\dmp]+)'
        r'_c(?P<c>[\dmp]+)'
        r'_dps(?P<dps>\d+)'
        r'(?:_(?P<dtype>f64))?'
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
        'dtype': d['dtype'] or 'mp',
        'count': int(d['count']) if d['count'] else None,
    }


# ============================================================
#  ДИАЛОГ ВЫБОРА ФАЙЛОВ
# ============================================================
root = tk.Tk()
root.withdraw()

input_dir = 'Portraits/CSV'
if not os.path.isdir(input_dir):
    input_dir = os.getcwd()

print("📂 Выберите CSV-файлы для наложения...")

filepaths = filedialog.askopenfilenames(
    title="Выберите CSV для наложения",
    initialdir=os.path.abspath(input_dir),
    filetypes=[("CSV files", "*.csv"), ("All files", "*.*")]
)

if not filepaths:
    print("❌ Файлы не выбраны. Выход.")
    exit()

print(f"✅ Выбрано файлов: {len(filepaths)}\n")


# ============================================================
#  РУЧНОЕ ПЕРЕИМЕНОВАНИЕ (Способ 2)
# ============================================================
print("🏷️ Настройка названий для легенды")
print("   (Enter — оставить по умолчанию, Cancel — тоже)\n")

labels = []

for i, filepath in enumerate(filepaths, 1):
    filename = os.path.basename(filepath)
    info = parse_params_from_filename(filename)

    if info:
        default_label = (
            f"a={info['a']}, c={info['c']} "
            f"({info['dtype']}, dps={info['dps']}, N={info['count']})"
        )
    else:
        default_label = filename

    user_label = ask_string_custom(
        title=f"Файл {i} из {len(filepaths)}",
        prompt=f"Файл:\n{filename}\n\nВведите название для легенды:",
        initialvalue=default_label
    )

    if not user_label or not user_label.strip():
        final_label = default_label
    else:
        final_label = user_label.strip()

    labels.append(final_label)
    print(f"  [{i}] {final_label}")

print("\n✅ Названия назначены:")
for fp, lab in zip(filepaths, labels):
    print(f"  {os.path.basename(fp)}\n    → «{lab}»")


# ============================================================
#  ЦВЕТА
# ============================================================
COLORS = [
    'green', 'red', 'blue', 'orange', 'purple',
    'brown', 'magenta', 'cyan', 'black', 'olive',
    'teal', 'navy', 'maroon', 'lime', 'gold',
]


# ============================================================
#  ОТРИСОВКА
# ============================================================
plt.rcParams['figure.dpi'] = 300
plt.rcParams['savefig.dpi'] = 300
plt.rcParams['font.size'] = 11

fig, ax = plt.subplots(figsize=(12, 10))

for idx, filepath in enumerate(filepaths):
    filename = os.path.basename(filepath)
    df = load_csv(filepath)
    if df.empty:
        print(f"⚠️ {filename} пуст, пропускаем")
        continue

    color = COLORS[idx % len(COLORS)]

    ax.plot(
        df['x'], df['y'],
        linestyle='none',
        marker='.',
        markersize=0.99,
        markeredgewidth=0,
        alpha=1.0,
        color=color,
        label=labels[idx],
        rasterized=True,
    )

ax.set_title("Сравнение фазовых портретов | ")
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.grid(alpha=0.3)

ax.legend(
    loc='upper right',
    fontsize=9,
    title='Параметры',
    title_fontsize=11,
    markerscale=15,
    framealpha=0.9,
    facecolor='white',
    edgecolor='gray',
)

output_dir = 'Portraits/Pictures'
os.makedirs(output_dir, exist_ok=True)
out_path = os.path.join(output_dir, 'compare_overlay.png')

plt.savefig(out_path, dpi=300, bbox_inches='tight', facecolor='white')
print(f"\n✅ Сохранено: {out_path}")

# plt.show()  # раскомментируйте, если хотите увидеть окно