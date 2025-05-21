import matplotlib.pyplot as plt
import numpy as np
from mpmath import mp
from sys import stdout

mp.dps = 30
# Бифуркационное дерево динамической системы


def Henon(x, A, B, C):
    dx = mp.matrix([[0, 0, 0]])
    dx[0] = x[1]
    dx[1] = x[2]
    dx[2] = B * x[0] + A * x[2] + C * x[1] - x[1] ** 2
    return dx


A = mp.mpf('2.05')
B = mp.mpf('0.5')
C = mp.mpf('-1.89')

fx = []
fy = []
fz = []

fx1 = []
fy1 = []
fz1 = []

r = []

for j in range(500):
    stdout.write("\r%d" % j)
    stdout.flush()

    x = mp.matrix([[mp.mpf('0.1'), mp.mpf('0.1'), mp.mpf('0.1')]])

    for i in range(100):
        x = Henon(x, A, B, C)

    for i in range(10_000):
        x = Henon(x, A, B, C)

        # fx.append(x[0])
        # fy.append(x[1])
        # fz.append(x[2])

        if -5*10**(-4) <= x[1] <= 5*10**(-4) and x[0] >= 0:
            fx1.append(x[0])
            fy1.append(x[1])
            fz1.append(x[2])
            r.append(A)

    A -= 2*10**(-4)

# fp1 = np.linspace(-1.005, -1.005, 100) # NS
# fp2 = np.linspace(-1.167, -1.167, 100) # C-4
# fp3 = np.linspace(-1.42, -1.42, 100) # C-8
# fp4 = np.linspace(-1.5014, -1.5014, 100) # C-16
#
# fp5 = np.linspace(-1.5228, -1.5228, 100) # C-32
# fp6 = np.linspace(-1.527, -1.527, 100) # C-64
# fp7 = np.linspace(-1.528, -1.528, 100) # CH
# fp8 = np.linspace(-1.619, -1.619, 100) # HC

print(' ')
# print(fx)
# print(fy)
# print(fz)

# print(fx1)
# print(fy1)
# print(fz1)

fig, ax = plt.subplots()
ax.plot(r, fz1, 'r.', ms=0.5)

# a1 = np.linspace(-2.5, 1, 100)

# line1, = ax.plot(fp1, a1, label='NS')
# line2, = ax.plot(fp2, a1, label='C-4')
# line3, = ax.plot(fp3, a1, label='C-8')
# line4, = ax.plot(fp4, a1, label='C-16')
#
# line5, = ax.plot(fp5, a1, label='C-32')
# line6, = ax.plot(fp6, a1, label='C-64')
# line7, = ax.plot(fp7, a1, label='CH')
# line8, = ax.plot(fp8, a1, label='HC')

# ax.annotate('NS', xy=(-1.005, 0), xytext=(-0.95, -0.25),
#             arrowprops=dict(facecolor='black', shrink=0.05))
# ax.annotate('C-4', xy=(-1.167, -0.55), xytext=(-1.12, -0.55),
#             arrowprops=dict(facecolor='black', shrink=0.05))
# ax.annotate('C-8', xy=(-1.42, -0.97), xytext=(-1.38, -0.97),
#             arrowprops=dict(facecolor='black', shrink=0.05))
# ax.annotate('C-16', xy=(-1.5014, -1.252), xytext=(-1.465, -1.252),
#             arrowprops=dict(facecolor='black', shrink=0.05))
#
# ax.annotate('C-32', xy=(-1.5228, -1.318), xytext=(-1.465, -1.318),
#             arrowprops=dict(facecolor='black', shrink=0.05))
# ax.annotate('CH', xy=(-1.528, -1.328), xytext=(-1.465, -1.5),
#             arrowprops=dict(facecolor='black', shrink=0.05))
# ax.annotate('HC', xy=(-1.619, -1.656), xytext=(-1.57, -1.7),
#             arrowprops=dict(facecolor='black', shrink=0.05))

ax.grid()
# ax.legend()

ax.set_title(f'Бифуркационное дерево системы с параметрами C = {C}, B = {B}')
ax.set_xlabel('Параметр A')
ax.set_ylabel('X')

plt.show()