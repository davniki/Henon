import matplotlib.pyplot as plt
import numpy as np
from Lyp_exp2 import lyp_exp
import sys


def main():
    # Параметры сетки
    delta = 0.01

    a_min, a_max = 0.92, 2.12
    c_min, c_max = -2, -1.64
    b = 0.5

    # Создание сетки параметров
    a_n = np.linspace(a_min, a_max, 101)  # 20 интервалов -> 21 точка
    c_n = np.linspace(c_min, c_max, 101)

    # Предварительное вычисление всех показателей Ляпунова
    map_Henon = compute_lyapunov_map(a_n, c_n, b)

    # Визуализация
    plot_results(map_Henon, a_min, a_max, c_min, c_max, a_n, c_n)


def compute_lyapunov_map(a_n, c_n, b):
    """Вычисление карты показателей Ляпунова"""
    n_a, n_c = len(a_n), len(c_n)
    map_Henon = np.zeros((n_a, n_c))

    # Векторизованные вычисления
    A, C = np.meshgrid(a_n, c_n, indexing='ij')

    for i, a in enumerate(a_n):

        for j, c in enumerate(c_n):
            sys.stdout.write(f"\rProgress: {j + 1}/{len(c_n)}, {i + 1}/{len(a_n)}")
            sys.stdout.flush()

            x0 = np.array([0.1, 0.1, 0.1])
            lexp = lyp_exp(x0, a, b, c)
            map_Henon[i, j] = classify_lyapunov_exponents(lexp)

    return map_Henon


def classify_lyapunov_exponents(lexp, epsilon=0.001):
    """Классификация показателей Ляпунова"""
    l0, l1, l2 = lexp

    # Проверка условий в порядке убывания сложности
    if l0 < -epsilon and l1 < -epsilon and l2 < -epsilon:
        return 0
    elif abs(l0) < epsilon and l1 < -epsilon and l2 < -epsilon:
        return 1
    elif abs(l0) < epsilon and abs(l1) < epsilon and l2 < -epsilon:
        return 2
    # Исправление: в оригинале условие для 3 было идентично условию для 2
    elif l0 > epsilon and abs(l1) < epsilon and l2 < -epsilon:
        return 3
    else:
        return 4


def plot_results(map_Henon, a_min, a_max, c_min, c_max, a_n, c_n):
    """Визуализация результатов"""
    plt.figure(figsize=(10, 8))

    # Правильное вычисление aspect ratio
    a_range = a_max - a_min
    c_range = c_max - c_min
    aspect_ratio = a_range / c_range

    im = plt.imshow(map_Henon.T,  # транспонируем для правильной ориентации
                    cmap='jet',
                    origin='lower',
                    extent=[a_min, a_max, c_min, c_max],
                    aspect=aspect_ratio)

    plt.colorbar(im, label='Класс показателей Ляпунова')
    plt.xlabel('Параметр a')
    plt.ylabel('Параметр c')
    plt.title('Карта показателей Ляпунова для отображения Эно')
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()