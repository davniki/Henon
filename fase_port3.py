# import matplotlib.animation as animation
# import matplotlib.pyplot as plt
# import mpmath as mp
# import numpy as np
# from models import Henon
#
# from mpmath import mp
# mp.dps = 25
#
# a = mp.mpf('1.43')
# b = mp.mpf('0.5')
# # c = mp.mpf('-1.75941488')
# c= mp.mpf('-1.7')
# t = 10_000
# iterations = np.linspace(0, t)
#
# x = [mp.mpf('0.1'), mp.mpf('0.1'), mp.mpf('0.1')]
#
# fx = []
# fy = []
# fz = []
#
# for i in range(1000):
#     x = Henon(x, a, b, c)
#
# for i in iterations:
#     x = Henon(x, a, b, c)
#     fx.append(x[0])
#     fy.append(x[1])
#     fz.append(x[2])
#
# fig, ax = plt.subplots()
#
# line = ax.scatter(fx, fy, hatch='.', color='green', s=0.5)
#
#
# def update(frame):
#     x = fx[:frame]
#     y = fy[:frame]
#     # update the scatter plot:
#     data = np.stack([x, y]).T
#     line.set_offsets(data)
#     return line
#
#
# animate = animation.FuncAnimation(fig=fig, func=update, interval=30, frames=200)
#
# plt.show()
#
# # animate.save('fp_ani.mp4', writer = 'ffmpeg', fps = 30)

# import matplotlib.animation as animation
# import matplotlib.pyplot as plt
# import mpmath as mp
# import numpy as np
# from models import Henon
#
# mp.dps = 25
#
# # Параметры
# a = mp.mpf('1.43')
# b = mp.mpf('0.5')
# # c = mp.mpf('-1.7')
# c = mp.mpf('-1.75941488')
# t = 1_000_000
#
# # Инициализация
# x = [mp.mpf('0.1'), mp.mpf('0.1'), mp.mpf('0.1')]
# fx, fy, fz = [], [], []
#
# # "Прогрев" системы
# for _ in range(1000):
#     x = Henon(x, a, b, c)
#
# # Основные итерации
# for _ in range(t):
#     x = Henon(x, a, b, c)
#     fx.append(float(x[0]))  # Конвертируем в float для matplotlib
#     fy.append(float(x[1]))
#     fz.append(float(x[2]))
#
# # Создание анимации
# fig, ax = plt.subplots(figsize=(10, 8))
# ax.set_xlim(min(fx), max(fx))
# ax.set_ylim(min(fy), max(fy))
# ax.set_xlabel('X')
# ax.set_ylabel('Y')
# ax.set_title('Аттрактор Хенона')
#
# # Используем Line2D для более эффективной анимации
# line, = ax.plot([], [], '.', color='green', markersize=1, alpha=0.3)
#
# def update(frame):
#     # Показываем точки постепенно
#     display_points = min(frame * 50, len(fx))  # Показываем по 50 точек за кадр
#     line.set_data(fx[:display_points], fy[:display_points])
#     return line,
#
# # Анимация
# animate = animation.FuncAnimation(
#     fig=fig,
#     func=update,
#     frames=t,
#     interval=30,
#     blit=True,  # Ускоряет анимацию
#     repeat=True
# )
#
# plt.tight_layout()
# plt.show()

# import matplotlib.animation as animation
# import matplotlib.pyplot as plt
# import mpmath as mp
# import numpy as np
# from models import Henon
#
# mp.dps = 25
#
# # Параметры
# a = mp.mpf('1.43')
# b = mp.mpf('0.5')
# # c = mp.mpf('-1.7')
# c = mp.mpf('-1.75941488')
# t = 10_000
#
# # Инициализация
# x = [mp.mpf('0.1'), mp.mpf('0.1'), mp.mpf('0.1')]
# fx, fy, fz = [], [], []
#
# # "Прогрев" системы
# for _ in range(1000):
#     x = Henon(x, a, b, c)
#
# # Основные итерации
# for _ in range(t):
#     x = Henon(x, a, b, c)
#     fx.append(x[0])
#     fy.append(x[1])
#     fz.append(x[2])
#
# # Создание анимации
# fig, ax = plt.subplots(figsize=(10, 8))
#
# # Устанавливаем пределы графика
# ax.set_xlim(float(min(fx)), float(max(fx)))
# ax.set_ylim(float(min(fy)), float(max(fy)))
# ax.set_xlabel('X')
# ax.set_ylabel('Y')
# ax.set_title(f'Аттрактор Хенона ({t} точек)')
#
# # Используем Line2D для эффективной анимации
# line, = ax.plot([], [], '.', color='green', markersize=0.5, alpha=0.7)
#
#
# def update(frame):
#     # Показываем все точки до текущего кадра
#     # Каждый кадр показывает больше точек
#     display_points = min(frame + 1, t)  # +1 чтобы начать с 1 точки
#
#     # Конвертируем только отображаемые данные
#     x_display = [float(x_i) for x_i in fx[:display_points]]
#     y_display = [float(y_i) for y_i in fy[:display_points]]
#
#     line.set_data(x_display, y_display)
#
#     # Добавляем счетчик точек
#     if hasattr(update, 'text'):
#         update.text.remove()
#     update.text = ax.text(0.02, 0.98, f'Точек: {display_points}/{t}',
#                           transform=ax.transAxes, verticalalignment='top',
#                           bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
#
#     return line, update.text
#
#
# # Инициализируем текстовый объект
# update.text = ax.text(0.02, 0.98, f'Точек: 0/{t}',
#                       transform=ax.transAxes, verticalalignment='top',
#                       bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
#
# # Анимация - количество кадров равно количеству точек
# animate = animation.FuncAnimation(
#     fig=fig,
#     func=update,
#     frames=t,  # Теперь кадров столько же, сколько точек
#     interval=1,  # Уменьшаем интервал для плавной анимации
#     blit=True,
#     repeat=True
# )
#
# plt.tight_layout()
# plt.show()

import matplotlib.animation as animation
import matplotlib.pyplot as plt
import mpmath as mp
import numpy as np
from models import Henon

mp.dps = 25

# Параметры
a = mp.mpf('1.43')
b = mp.mpf('0.5')
c = mp.mpf('-1.75941488')
t = 10_000
points_per_frame = 5  # Меньше точек за кадр = медленнее
frame_interval = 200  # Больше интервал = медленнее

# Инициализация
x = [mp.mpf('0.1'), mp.mpf('0.1'), mp.mpf('0.1')]
fx, fy, fz = [], [], []

# "Прогрев" системы
for _ in range(1000):
    x = Henon(x, a, b, c)

# Основные итерации
for _ in range(t):
    x = Henon(x, a, b, c)
    fx.append(x[0])
    fy.append(x[1])
    fz.append(x[2])

# Создание анимации
fig, ax = plt.subplots(figsize=(7, 6))
ax.set_xlim(float(min(fx)), float(max(fx)))
ax.set_ylim(float(min(fy)), float(max(fy)))
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title(f'Аттрактор Хенона ({t} точек) - Медленная анимация')

# Создаем два scatter plot
old_points = ax.scatter([], [], color='green', s=0.5, alpha=0.7)
new_points = ax.scatter([], [], color='red', s=3, alpha=1.0)  # Увеличили размер красных точек


def update(frame):
    display_points = min((frame + 1) * points_per_frame, t)

    # Конвертируем все точки до текущего момента
    x_display = [float(x_i) for x_i in fx[:display_points]]
    y_display = [float(y_i) for y_i in fy[:display_points]]

    # Разделяем точки на старые и новые
    if display_points > points_per_frame:
        # Старые точки (все кроме последних points_per_frame)
        old_x = x_display[:-points_per_frame]
        old_y = y_display[:-points_per_frame]
        # Новые точки (последние points_per_frame)
        new_x = x_display[-points_per_frame:]
        new_y = y_display[-points_per_frame:]
    else:
        # Если точек меньше, чем points_per_frame, все считаем новыми
        old_x, old_y = [], []
        new_x, new_y = x_display, y_display

    # Обновляем данные
    old_points.set_offsets(np.c_[old_x, old_y])
    new_points.set_offsets(np.c_[new_x, new_y])

    # Обновляем счетчик
    if hasattr(update, 'text'):
        update.text.remove()
    update.text = ax.text(0.02, 0.98, f'Точек: {display_points}/{t}\nСкорость: {points_per_frame} точек/кадр',
                          transform=ax.transAxes, verticalalignment='top',
                          bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

    return old_points, new_points, update.text


# Инициализируем текстовый объект
update.text = ax.text(0.02, 0.98, f'Точек: 0/{t}\nСкорость: {points_per_frame} точек/кадр',
                      transform=ax.transAxes, verticalalignment='top',
                      bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

# Количество кадров
frames = (t + points_per_frame - 1) // points_per_frame

animate = animation.FuncAnimation(
    fig=fig,
    func=update,
    frames=frames,
    interval=frame_interval,  # Увеличили интервал между кадрами
    blit=True,
    repeat=True
)

plt.tight_layout()
plt.show()
