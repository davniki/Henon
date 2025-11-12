import numpy as np
from sys import stdout


# Спектр ляпуновских показателей


def Henon(x, A, B, C):
    # dx = np.array([0, 0, 0])
    dx0 = x[1]
    dx1 = x[2]
    dx2 = B * x[0] + A * x[2] + C * x[1] - x[1] ** 2
    return np.array([dx0, dx1, dx2])


def d_Henon(dx, x, A, B, C):
    # dx0 = np.array([0, 0, 0])
    dx0 = dx[1]
    dx1 = dx[2]
    dx2 = B * dx[0] + (C - 2 * x[1]) * dx[1] + A * dx[2]
    return np.array([dx0, dx1, dx2])


# m = 2500
# t = 25
#
# L_1 = 0
# L_2 = 0
# L_3 = 0
# c = []


# начальные вектора возмущения, которые ортоганальны и нормированы на еденицу
# dx = np.array([1, 0, 0])
# dy = np.array([0, 1, 0])
# dz = np.array([0, 0, 1])
#
# sum_1 = 0
# sum_2 = 0
# sum_3 = 0
#
# g_1 = 0
# g_2 = 0
# g_3 = 0


def lyp_exp(x, A, B, C):
    dx = np.array([1, 0, 0])
    dy = np.array([0, 1, 0])
    dz = np.array([0, 0, 1])

    m = 2500
    t = 25

    L_1 = 0
    L_2 = 0
    L_3 = 0
    c = []

    sum_1 = 0
    sum_2 = 0
    sum_3 = 0

    g_1 = 0
    g_2 = 0
    g_3 = 0

    for l in range(100):
        x = Henon(x, A, B, C)

    for j in range(m):
        # stdout.write("\r%d" % j)
        # stdout.flush()
        for i in range(t):
            x = Henon(x, A, B, C)
            dx = d_Henon(dx, x, A, B, C)
            dy = d_Henon(dy, x, A, B, C)
            dz = d_Henon(dz, x, A, B, C)

        if np.linalg.norm(dx, 2) != 0:
            sum_1 += np.log(np.linalg.norm(dx, 2))
            g_1 += 1
            dx = dx / np.linalg.norm(dx, 2)

        dy1 = dy - (dy @ dx.T) * dx
        if np.linalg.norm(dy1, 2) != 0:
            sum_2 += np.log(np.linalg.norm(dy1, 2))
            g_2 += 1
            dy = dy1 / np.linalg.norm(dy1, 2)

        dz1 = dz - (dz @ dx.T) * dx - (dz @ dy.T) * dy
        if np.linalg.norm(dz1, 2) != 0:
            sum_3 += np.log(np.linalg.norm(dz1, 2))
            g_3 += 1
            dz = dz1 / np.linalg.norm(dz1, 2)

    L_1 = sum_1 / (g_1 * t)
    L_2 = sum_2 / (g_2 * t)
    L_3 = sum_3 / (g_3 * t)

    return L_1, L_2, L_3

# A = 1.43
# B = 0.5
# C = -1.75941488
#
# x = np.array([0.1, 0.1, 0.1])
#
# print(lyp_exp(x, A, B, C))

# print(' ')
# print(L_1)
# print(L_2)
# print(L_3)
