import matplotlib.pyplot as plt
import numpy as np

from mpmath import mp
mp.dps = 25

###
#  Фазовый портрет динамической системы
###

# a = mp.mpf('1.42')
# b = mp.mpf('0.5')
# c = mp.mpf('-1.7574339')

a = mp.mpf('1.43')
b = mp.mpf('0.5')
c = mp.mpf('-1.45')

def Henon(x, A, B, C):
    dx = mp.matrix([[0, 0, 0]])
    dx[0] = x[1]
    dx[1] = x[2]
    dx[2] = B * x[0] + A * x[2] + C * x[1] - x[1] ** 2
    return dx


# x0 = 0.1
# y0 = 0.2
# z0 = 0.3

x = [mp.mpf('0.1'), mp.mpf('0.1'), mp.mpf('0.1')]

fx = []
fy = []
fz = []

fx1 = []
fy1 = []
fz1 = []

k = 0

for i in range(50_000):
    x = Henon(x, a, b, c)

for i in range(2_000_000):
    x = Henon(x, a, b, c)

    fx.append(x[0])
    fy.append(x[1])
    fz.append(x[2])

    if (-0.45 < x[0] < -0.3) and (-0.5 < x[1] < -0.35):
        fx1.append(x[0])
        fy1.append(x[1])
        fz1.append(x[2])

        k += 1

# a = mp.mpf('1.42')
# b = mp.mpf('0.5')
# c = mp.mpf('-1.757435')
#
# fx2 = []
# fy2 = []
# fz2 = []
#
# x = [mp.mpf('0.1'), mp.mpf('0.1'), mp.mpf('0.1')]
#
# for i in range(100_000):
#     x = Henon(x, a, b, c)
#
# for i in range(1_000_000):
#     x = Henon(x, a, b, c)
#     fx2.append(x[0])
#     fy2.append(x[1])
#     fz2.append(x[2])

# m = 0
#
# while k != 100_000:
#     x = Henon(x, a, b, c)
#
#     fx.append(x[0])
#     fy.append(x[1])
#     fz.append(x[2])
#
#     m += 1
#
#     if (-0.45 < x[0] < -0.3) and (-0.5 < x[1] < -0.35):
#         fx1.append(x[0])
#         fy1.append(x[1])
#         fz1.append(x[2])
#
#         k += 1

# print(m)
# print(k)

fig, ax = plt.subplots()
fig, ax1 = plt.subplots()

ax.plot(fx, fy, 'g.')
# ax.plot(fx2, fy2, 'r.', ms=0.1)

ax1.plot(fx1, fy1, 'g.', ms=0.3)

ax.set_title(f'A = {a}, B = {b}, C = {c}')
ax.grid()
ax.set_xlabel('X')
ax.set_ylabel('Y')

ax1.set_title(f'A = {a}, B = {b}, C = {c}')
ax1.grid()
ax1.set_xlabel('X')
ax1.set_ylabel('Y')

plt.show()
# plt.savefig(f'fase_port_a_{a}_c_{c}.eps', format='eps')
