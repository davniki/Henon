import matplotlib.pyplot as plt
import pandas as pd
import os

# --- ЗАГРУЗКА ---
input_dir = 'Portraits'


def load_csv(filepath):
    """Загружает CSV, пропуская строки-комментарии."""
    df = pd.read_csv(filepath, comment='#')
    return df


df_full = load_csv(os.path.join(input_dir, 'phase_full.csv'))
df_zoom1 = load_csv(os.path.join(input_dir, 'phase_zoom1.csv'))
df_zoom2 = load_csv(os.path.join(input_dir, 'phase_zoom2.csv'))

# --- НАСТРОЙКИ КАЧЕСТВА ---
plt.rcParams['figure.dpi'] = 600
plt.rcParams['savefig.dpi'] = 600
plt.rcParams['font.size'] = 12

# --- ОТРИСОВКА ---
plots = [
    (df_full, 'phase_portrait_full', 'Полный портрет'),
    (df_zoom1, 'phase_portrait_zoom1', 'Увеличение 1'),
    (df_zoom2, 'phase_portrait_zoom2', 'Увеличение 2'),
]

output_dir = 'Portraits'
os.makedirs(output_dir, exist_ok=True)

for df, name, title in plots:
    fig, ax = plt.subplots()

    # Ключевые настройки против "смазывания":
    ax.plot(
        df['x'], df['y'],
        linestyle='none',
        marker='.',
        markersize=0.7,  # очень маленькие точки
        markeredgewidth=0,  # без обводки
        alpha=1.0,  # без прозрачности
        color='green',
        rasterized=True,  # растеризация при сохранении в PDF/SVG
    )

    ax.set_title(f'{title}')
    ax.grid(alpha=0.3)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')

    # Сохраняем
    filepath = os.path.join(output_dir, f'{name}.png')
    plt.savefig(filepath, dpi=600, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    print(f"✅ {filepath}")
    plt.close()

print("🎉 Готово!")
