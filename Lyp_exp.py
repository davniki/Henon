import matplotlib.pyplot as plt
import numpy as np
from sys import stdout
from mpmath import mp

mp.dps = 30
# Спектр ляпуновских показателей


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


A = mp.mpf('1.990915')
B = mp.mpf('0.5')
C = mp.mpf('-1.89')

m = 2500
t = 25

L_1 = 0
L_2 = 0
L_3 = 0
c = []


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

for l in range(100):
    x = Henon(x, A, B, C)

for j in range(m):
    stdout.write("\r%d" % j)
    stdout.flush()
    for i in range(t):
        x = Henon(x, A, B, C)
        dx = d_Henon(dx, x, A, B, C)
        dy = d_Henon(dy, x, A, B, C)
        dz = d_Henon(dz, x, A, B, C)

    if mp.norm(dx, 2) != 0:
        sum_1 += mp.log(mp.norm(dx, 2))
        g_1 += 1
        dx = dx / mp.norm(dx, 2)

    dy1 = dy - (dy * dx.T)[0] * dx
    if mp.norm(dy1, 2) != 0:
        sum_2 += mp.log(mp.norm(dy1, 2))
        g_2 += 1
        dy = dy1 / mp.norm(dy1, 2)

    dz1 = dz - (dz * dx.T)[0] * dx - (dz * dy.T)[0] * dy
    if mp.norm(dz1, 2) != 0:
        sum_3 += mp.log(mp.norm(dz1, 2))
        g_3 += 1
        dz = dz1 / mp.norm(dz1, 2)

L_1 = sum_1 / (g_1 * t)
L_2 = sum_2 / (g_2 * t)
L_3 = sum_3 / (g_3 * t)

print(' ')
print(L_1)
print(L_2)
print(L_3)