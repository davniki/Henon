import numpy as np
import math as mt
import matplotlib.pyplot as plt
from mpmath import mp
# mp.dps = 20
# gcV = mp.mpf('0.07')

# Старший ляпуновский показатель

A = 0
B = 0.1
C = -0.8

m = 100
t = 10

L = []
c = []

for j in range(100):
    x0 = 0.1
    y0 = 0.2
    z0 = 0.3
    dx0 = 0.01 + x0
    dy0 = 0.01 + y0
    dz0 = 0.01 + z0
    x = 0
    y = 0
    z = 0
    dx = 0
    dy = 0
    dz = 0
    eps = mt.sqrt(dx0 ** 2 + dy0 ** 2 + dz0 ** 2)
    sum = 0
    g = 0

    for l in range(300):
        z = B * x0 + A * z0 + C * y0 - y0 ** 2
        x = y0
        y = z0

        z0 = z
        x0 = x
        y0 = y
    for j in range(m):
        for i in range(t):
            x = y0
            y = z0
            z = B * x0 + (C - y0) * y0 + A * z0

            z0 = z
            x0 = x
            y0 = y

            dx = dy0
            dy = dz0
            dz = B * dx0 + (C - 2 * y0) * dy0 + A * dz0

            dz0 = dz
            dx0 = dx
            dy0 = dy

        f = mt.sqrt(dx0 ** 2 + dy0 ** 2 + dz0 ** 2)
        if f != 0:
            k = mt.log(f / eps)
            sum += k
            g += 1

            dx0 = (eps * dx0) / f
            dy0 = (eps * dy0) / f
            dz0 = (eps * dz0) / f

    L.append(sum/(g*t))
    c.append(C)
    C -= 0.01

fig, ax = plt.subplots()
ax.plot(c, L)
ax.grid()

plt.show()
print(L)
