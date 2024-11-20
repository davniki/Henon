# import numpy as np
import matplotlib.pyplot as plt
from mpmath import mp

mp.dps = 10

# Решение задачи Коши методом Эйлера

# Дано дифференциальное уравнение:
# dx1/dt = f1(x_1, ..., x_k, t)
# ...
# dxk/dt = fn(x1, ..., x_k, t)
# ,где (x_1, ..., x_k) = x

# Для него также даны начальные условия:
# x_0 = x(t_0)

# Нужно найти траекторию на промежутке времен t \in [t_0, t_end]

# Метод Эйлера:
# (x(t_n+1) - x(t_n)) / (t_n+1 - t_n) = f(x_n, t_n), dt = t_n+1 - t_n -> 0

# x(t_n+1) = x(t_n) + f(x_n, t_n)*dt

# Example. Lorenz system:
# dx/dt = sigma*(y - x)
# dy/dt = x*(ro - z) - y
# dz/dt = x*y - beta*z


def lorenz(x, sigma, ro, beta):
    dx = mp.matrix([0, 0, 0])
    dx[0] = sigma*(x[1] - x[0])
    dx[1] = x[0]*(ro - x[2]) - x[1]
    dx[2] = x[0]*x[1] - beta*x[2]
    return dx


x = mp.matrix([mp.mpf('0'), mp.mpf('1'), mp.mpf('1.05')])

s = mp.mpf('10')
r = mp.mpf('28')
b = mp.mpf('8/3')

dt = 0.01  # шаг интервала
N = 10_000

T = []
fx = []
fy = []
fz = []

for i in range(N):
    x = x + (lorenz(x, s, r, b) * dt)
    print(x)
    fx.append(x[0])
    fy.append(x[1])
    fz.append(x[2])
    T.append(i*dt)

# print(T, fy, fz)
ax = plt.figure().add_subplot(projection='3d')

ax.plot(fx, fy, fz, ms=0.1)
ax.grid()

plt.show()
