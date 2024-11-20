import numpy as np
# import math as mt
import matplotlib.pyplot as plt

from mpmath import mp
mp.dps = 30

A = mp.mpf('-0.227')
B = mp.mpf('-0.5')
C = [mp.mpf('-1.375')]

m = 1000
t = 10

L_1 = []
L_2 = []
L_3 = []


def Henon(x, A, B, C):
    dx = mp.matrix([[0, 0, 0]])
    dx[0] = x[1]
    dx[1] = x[2]
    dx[2] = B * x[0] + A * x[2] + C * x[1] - x[1] ** 2
    return dx


def d_Henon(dx, x, A, B, C):
    dx0 = mp.matrix([[0, 0, 0]])
    dx0[0] = dx[1]
    dx0[1] = dx[2]
    dx0[2] = B * dx[0] + (C - 2 * x[1]) * dx[1] + A * dx[2]
    return dx0


for q in range(len(C)):
    x = mp.matrix([[mp.mpf('0.1'), mp.mpf('0.1'), mp.mpf('0.1')]])

    # начальные вектора возмущения, которые ортоганальны и нормированы на еденицу
    dx = mp.matrix([[mp.mpf('1'), 0, 0]])
    dy = mp.matrix([[0, mp.mpf('1'), 0]])
    dz = mp.matrix([[0, 0, mp.mpf('1')]])

    sum_1 = 0
    sum_2 = 0
    sum_3 = 0

    g_1 = 0
    g_2 = 0
    g_3 = 0

    for l in range(300):
        x = Henon(x, A, B, C[q])

    for j in range(m):
        for i in range(t):
            x = Henon(x, A, B, C[q])
            dx = d_Henon(dx, x, A, B, C[q])
            dy = d_Henon(dy, x, A, B, C[q])
            dz = d_Henon(dz, x, A, B, C[q])

        if mp.norm(dx, 2) != 0:
            sum_1 += mp.log(mp.norm(dx, 2))
            g_1 += 1
            dx = dx / mp.norm(dx, 2)

        dy1 = dy - (dy * dx.T)[0] * dx
        if mp.norm(dy1, 2) != 0:
            sum_2 += mp.log(mp.norm(dy1, 2))
            g_2 += 1
            dy = dy1 / mp.norm(dy1, 2)

        dz1 = dz - (dz*dx.T)[0] * dx - (dz*dy.T)[0] * dy
        if mp.norm(dz1, 2) != 0:
            sum_3 += mp.log(mp.norm(dz1, 2))
            g_3 += 1
            dz = dz1 / mp.norm(dz1, 2)

    L_1.append(sum_1 / (g_1 * t))
    L_2.append(sum_2 / (g_2 * t))
    L_3.append(sum_3 / (g_3 * t))

print(C)
print(L_1)
print(L_2)
print(L_3)

# fig, ax = plt.subplots()
# l1 = ax.plot(c, L_1, label='L-1')
# l2 = ax.plot(c, L_2, label='L-2')
# l3 = ax.plot(c, L_3, label='L-3')
# ax.grid()
# ax.legend()
# ax.set_title(f"A = {A}, B = {B}")
# ax.set_xlabel("Параметр C")
# ax.set_ylabel("Показатель Ляпунова L")
# plt.show()