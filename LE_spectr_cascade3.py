import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap, BoundaryNorm

# Загружаем данные
df = pd.read_csv('lyapunov_map.csv', index_col=0)

# Преобразуем в матрицу
matrix = df.values

# Получаем значения параметров
A_values = df.columns.astype(float)  # параметр A по горизонтали
C_values = df.index.astype(float)    # параметр C по вертикали

# Создаем свою цветовую карту с 7 фиксированными цветами
# 0 - синий
# 1 - зеленый
# 2 - желтый
# 3 - красный
# 4 - розовый
# 5 - бирюзовый
# 6 - белый
colors = ['blue', 'green', 'yellow', 'red', 'pink', 'cyan', 'white']
cmap = ListedColormap(colors)

# Границы для каждого режима (для 7 режимов от 0 до 6)
bounds = [-0.5, 0.5, 1.5, 2.5, 3.5, 4.5, 5.5, 6.5]
norm = BoundaryNorm(bounds, cmap.N)

# Создаем фигуру с дополнительным местом справа для легенды
fig, ax = plt.subplots(figsize=(14, 8))  # Увеличили ширину с 12 до 14

# Отображаем матрицу как изображение с фиксированными цветами
im = ax.imshow(matrix, cmap=cmap, norm=norm, origin='lower',
               extent=[A_values.min(), A_values.max(), C_values.min(), C_values.max()], aspect='auto',
               interpolation='nearest')

# Добавляем цветовую шкалу с подписями режимов
cbar = plt.colorbar(im, ax=ax, ticks=[0, 1, 2, 3, 4, 5, 6], fraction=0.046, pad=0.04)
cbar.set_label('Режим', fontsize=12)

# Подписи осей
ax.set_xlabel('Параметр A', fontsize=14)
ax.set_ylabel('Параметр C', fontsize=14)
ax.set_title('Карта Ляпуновских показателей обобщенного трехмерного отображения Мира', fontsize=16)

# ===== ДОБАВЛЯЕМ ОРАНЖЕВУЮ ЛИНИЮ ДЛЯ A = 1.43 =====
a_value = 1.43  # значение параметра A, которое нужно отметить

# Проверяем, что значение входит в диапазон
if A_values.min() <= a_value <= A_values.max():
    # Добавляем вертикальную линию
    ax.axvline(x=a_value, color='orange', linewidth=2, linestyle='--',
               label=f'A = {a_value}')

    # Добавляем текст с подписью
    # ax.text(a_value + 0.05, C_values.max() - 0.1, f'A = {a_value}',
    #         color='orange', fontsize=12, fontweight='bold',
    #         bbox=dict(facecolor='white', alpha=0.7, edgecolor='orange'))
else:
    print(f"⚠️ Значение A = {a_value} вне диапазона [{A_values.min()}, {A_values.max()}]")
# ===== КОНЕЦ БЛОКА С ЛИНИЕЙ =====

# Добавляем легенду для расшифровки цветов
from matplotlib.patches import Patch
legend_elements = [Patch(facecolor='blue', label='0: Неподвижная точка'),
                   Patch(facecolor='green', label='1: Инвариантная кривая'),
                   Patch(facecolor='yellow', label='2: Бифуркация удвоения периода ИК'),
                   Patch(facecolor='red', label='3: Хаос'), Patch(facecolor='pink', label='4: Хаос с нулем'),
                   Patch(facecolor='cyan', label='5: Гипперхаос'),
                   Patch(facecolor='white', edgecolor='black', label='6: Другое'),
                   Patch(facecolor='none', edgecolor='orange',
                         linestyle='--', label=f'A = {a_value}')]

# Добавляем элемент для оранжевой линии в легенду

# Размещаем легенду справа от графика
ax.legend(handles=legend_elements,
          bbox_to_anchor=(1.25, 1.0),  # Увеличили с 1.05 до 1.25
          loc='upper left',
          borderaxespad=0.,
          fontsize=10,
          title='Режимы',
          title_fontsize=12)

# Настраиваем отступы
plt.tight_layout()
plt.subplots_adjust(right=0.75)  # Увеличиваем правый отступ

# Сохраняем картинку
plt.savefig('lyapunov_map.png', dpi=300, bbox_inches='tight')
print("✅ Картинка сохранена как 'lyapunov_map.png'")

plt.show()

# Выводим информацию о матрице
print(f"Размер матрицы: {matrix.shape[0]} x {matrix.shape[1]}")
print(f"Диапазон A: [{A_values.min():.2f}, {A_values.max():.2f}]")
print(f"Диапазон C: [{C_values.min():.2f}, {C_values.max():.2f}]")
print(f"Уникальные значения в матрице: {np.unique(matrix)}")
print(f"\n🔸 Отмечена вертикальная линия при A = {a_value}")

# Статистика по режимам
unique, counts = np.unique(matrix, return_counts=True)
print("\nСтатистика режимов:")
mode_names = {
    0: "Неподвижная точка",
    1: "Инвариантная кривая",
    2: "Бифуркация удвоения периода ИК",
    3: "Хаос",
    4: "Хаос с нулем",
    5: "Гипперхаос",
    6: "Другое"
}
for mode, count in zip(unique, counts):
    name = mode_names.get(mode, f"Неизвестный режим {mode}")
    print(f"  Режим {int(mode)} ({name}): {count} точек ({count/matrix.size*100:.1f}%)")
