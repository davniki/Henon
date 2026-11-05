# models_numpy.py
import numpy as np


def henon(x, a, b, c):
    """
    Numpy-версия 3D-отображения Эно.
    x — np.array([x0, x1, x2], dtype=np.float64)
    Возвращает np.array([x0', x1', x2'], dtype=np.float64)
    """
    x0, x1, x2 = x
    x0_new = x1
    x1_new = x2
    x2_new = b * x0 + a * x2 + c * x1 - x1 ** 2
    return np.array([x0_new, x1_new, x2_new], dtype=np.float64)


def d_henon(dx, x, a, b, c):
    """
    Numpy-версия матрицы Якоби, применённой к вектору возмущения dx.
    dx — np.array([dx0, dx1, dx2], dtype=np.float64)
    """
    dx0, dx1, dx2 = dx
    x0, x1, x2 = x
    dx0_new = dx1
    dx1_new = dx2
    dx2_new = b * dx0 + (c - 2 * x1) * dx1 + a * dx2
    return np.array([dx0_new, dx1_new, dx2_new], dtype=np.float64)


def lyp_exp(x, a, b, c):
    """
    Numpy-версия вычисления показателей Ляпунова.
    x — np.array([x0, x1, x2], dtype=np.float64)
    """
    # Начальные векторы возмущения (ортонормированные)
    dx = np.array([1.0, 0.0, 0.0], dtype=np.float64)
    dy = np.array([0.0, 1.0, 0.0], dtype=np.float64)
    dz = np.array([0.0, 0.0, 1.0], dtype=np.float64)

    m = 2000
    t = 20

    l_1 = l_2 = l_3 = 0
    sum_1 = sum_2 = sum_3 = 0
    g_1 = g_2 = g_3 = 0

    # Транзиент
    for l in range(1000):
        x = henon(x, a, b, c)

    for j in range(m):
        for i in range(t):
            x = henon(x, a, b, c)
            dx = d_henon(dx, x, a, b, c)
            dy = d_henon(dy, x, a, b, c)
            dz = d_henon(dz, x, a, b, c)

        # Ортогонализация Грама — Шмидта
        norm_dx = np.linalg.norm(dx)
        if norm_dx != 0:
            sum_1 += np.log(norm_dx)
            g_1 += 1
            dx = dx / norm_dx

        dy1 = dy - np.dot(dy, dx) * dx
        norm_dy1 = np.linalg.norm(dy1)
        if norm_dy1 != 0:
            sum_2 += np.log(norm_dy1)
            g_2 += 1
            dy = dy1 / norm_dy1

        dz1 = dz - np.dot(dz, dx) * dx - np.dot(dz, dy) * dy
        norm_dz1 = np.linalg.norm(dz1)
        if norm_dz1 != 0:
            sum_3 += np.log(norm_dz1)
            g_3 += 1
            dz = dz1 / norm_dz1

    l_1 = sum_1 / (g_1 * t)
    l_2 = sum_2 / (g_2 * t)
    l_3 = sum_3 / (g_3 * t)

    return l_1, l_2, l_3