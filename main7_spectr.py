import matplotlib.pyplot as plt
import numpy as np
from mpmath import mp

mp.dps = 10
# Спектр ляпуновских показателей

A = mp.mpf('0.15')
B = mp.mpf('0.1')
C = mp.mpf('-1.8')

m = 1000
t = 10

L_1 = []
L_2 = []
L_3 = []
c = []


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


for q in range(1000):
    x = mp.matrix([[mp.mpf('0.1'), mp.mpf('0.2'), mp.mpf('0.3')]])

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
        x = Henon(x, A, B, C)

    for j in range(m):
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

        # dz1 = dz - (dz * dx.T)[0] * dx - (dz * dy.T)[0] * dy
        # if mp.norm(dz1, 2) != 0:
        #     sum_3 += mp.log(mp.norm(dz1, 2))
        #     g_3 += 1
        #     dz = dz1 / mp.norm(dz1, 2)

    L_1.append(sum_1 / (g_1 * t))
    L_2.append(sum_2 / (g_2 * t))
    # L_3.append(sum_3 / (g_3 * t))
    c.append(C)
    C += 0.0009

fp1 = np.linspace(-1.005, -1.005, 100) # NS
fp2 = np.linspace(-1.167, -1.167, 100) # C-4
fp3 = np.linspace(-1.42, -1.42, 100) # C-8
fp4 = np.linspace(-1.5014, -1.5014, 100) # C-16

fp5 = np.linspace(-1.5228, -1.5228, 100) # C-32
fp6 = np.linspace(-1.527, -1.527, 100) # C-64
fp7 = np.linspace(-1.528, -1.528, 100) # CH
fp8 = np.linspace(-1.619, -1.619, 100) # HC

fig, ax = plt.subplots()

a1 = np.linspace(-1.2, 0.2, 100)

l1 = ax.plot(c, L_1, label='L-1')
l2 = ax.plot(c, L_2, label='L-2')
# l3 = ax.plot(c, L_3, label='L-3')

line1, = ax.plot(fp1, a1, label='NS')
line2, = ax.plot(fp2, a1, label='C-4')
line3, = ax.plot(fp3, a1, label='C-8')
line4, = ax.plot(fp4, a1, label='C-16')

line5, = ax.plot(fp5, a1, label='C-32')
line6, = ax.plot(fp6, a1, label='C-64')
line7, = ax.plot(fp7, a1, label='CH')
line8, = ax.plot(fp8, a1, label='HC')

ax.annotate('NS', xy=(-1.005, 0), xytext=(-0.95, 0),
            arrowprops=dict(facecolor='black', shrink=0.05))
ax.annotate('C-4', xy=(-1.167, 0), xytext=(-1.12, 0.1),
            arrowprops=dict(facecolor='black', shrink=0.05))
ax.annotate('C-8', xy=(-1.42, 0), xytext=(-1.38, 0),
            arrowprops=dict(facecolor='black', shrink=0.05))
ax.annotate('C-16', xy=(-1.5014, 0), xytext=(-1.465, 0),
            arrowprops=dict(facecolor='black', shrink=0.05))

ax.annotate('C-32', xy=(-1.5228, 0), xytext=(-1.465, 0.066),
            arrowprops=dict(facecolor='black', shrink=0.05))
ax.annotate('CH', xy=(-1.528, 0), xytext=(-1.465, 0.133),
            arrowprops=dict(facecolor='black', shrink=0.05))
ax.annotate('HC', xy=(-1.619, 0), xytext=(-1.65, -0.066),
            arrowprops=dict(facecolor='black', shrink=0.05))
# ax.annotate('ICD-2', xy=(-1.759255, 0), xytext=(-1.725, 0.066),
#             arrowprops=dict(facecolor='black', shrink=0.05))

ax.grid()
ax.legend()
# ax.legend(handles=[line1, line2, line3, line4])
ax.set_title(f"A = {A}, B = {B}")
ax.set_xlabel("Параметр C")
ax.set_ylabel("Показатель Ляпунова L")
plt.show()
