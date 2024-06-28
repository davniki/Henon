import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math

def dx_dt(x, y, z):
    return y

def dy_dt(x, y, z):
    return P * math.cos(z) + mu*y - x *(1 + c2 * x + c3 * x**2)

def dz_dt(x, y, z):
    return w


def runge_kutta(u0, dt):
    N = 1 / dt
    x2, y2, z2 = u0
    j = 0
    while j < 50000:
        x, y, z = x2, y2, z2

        kx1 = dt * dx_dt(x, y, z)
        ky1 = dt * dy_dt(x, y, z)
        kz1 = dt * dz_dt(x, y, z)

        kx2 = dt * dx_dt(x + kx1 / 2, y + ky1 / 2, z + kz1 / 2)
        ky2 = dt * dy_dt(x + kx1 / 2, y + ky1 / 2, z + kz1 / 2)
        kz2 = dt * dz_dt(x + kx1 / 2, y + ky1 / 2, z + kz1 / 2)

        kx3 = dt * dx_dt(x + kx2 / 2, y + ky2 / 2, z + kz2 / 2)
        ky3 = dt * dy_dt(x + kx2 / 2, y + ky2 / 2, z + kz2 / 2)
        kz3 = dt * dz_dt(x + kx2 / 2, y + ky2 / 2, z + kz2 / 2)

        kx4 = dt * dx_dt(x + kx3, y + ky3, z + kz3)
        ky4 = dt * dy_dt(x + kx3, y + ky3, z + kz3)
        kz4 = dt * dz_dt(x + kx3, y + ky3, z + kz3)

        x2 = x + (kx1 + 2 * kx2 + 2 * kx3 + kx4) / 6
        y2 = y + (ky1 + 2 * ky2 + 2 * ky3 + ky4) / 6
        z2 = z + (kz1 + 2 * kz2 + 2 * kz3 + kz4) / 6

        j += 1

    i, j = 0, 0
    poinkare_section = [[], [], []]

    while j < 1000:
        x, y, z = x2, y2, z2

        kx1 = dt * dx_dt(x, y, z)
        ky1 = dt * dy_dt(x, y, z)
        kz1 = dt * dz_dt(x, y, z)

        kx2 = dt * dx_dt(x + kx1 / 2, y + ky1 / 2, z + kz1 / 2)
        ky2 = dt * dy_dt(x + kx1 / 2, y + ky1 / 2, z + kz1 / 2)
        kz2 = dt * dz_dt(x + kx1 / 2, y + ky1 / 2, z + kz1 / 2)

        kx3 = dt * dx_dt(x + kx2 / 2, y + ky2 / 2, z + kz2 / 2)
        ky3 = dt * dy_dt(x + kx2 / 2, y + ky2 / 2, z + kz2 / 2)
        kz3 = dt * dz_dt(x + kx2 / 2, y + ky2 / 2, z + kz2 / 2)

        kx4 = dt * dx_dt(x + kx3, y + ky3, z + kz3)
        ky4 = dt * dy_dt(x + kx3, y + ky3, z + kz3)
        kz4 = dt * dz_dt(x + kx3, y + ky3, z + kz3)

        x2 = x + (kx1 + 2 * kx2 + 2 * kx3 + kx4) / 6
        y2 = y + (ky1 + 2 * ky2 + 2 * ky3 + ky4) / 6
        z2 = z + (kz1 + 2 * kz2 + 2 * kz3 + kz4) / 6

        if j % N == 0:
            poinkare_section[0].append(x2)
            poinkare_section[1].append(y2)
            poinkare_section[2].append(z2)

        j += 1
    return poinkare_section


def runge_kutta2(u0, dt):
    N = 1 / dt
    x2, y2, z2 = u0
    j = 0
    while j < 50000:
        x, y, z = x2, y2, z2

        kx1 = dt * dx_dt(x, y, z)
        ky1 = dt * dy_dt(x, y, z)
        kz1 = dt * dz_dt(x, y, z)

        kx2 = dt * dx_dt(x + kx1 / 2, y + ky1 / 2, z + kz1 / 2)
        ky2 = dt * dy_dt(x + kx1 / 2, y + ky1 / 2, z + kz1 / 2)
        kz2 = dt * dz_dt(x + kx1 / 2, y + ky1 / 2, z + kz1 / 2)

        kx3 = dt * dx_dt(x + kx2 / 2, y + ky2 / 2, z + kz2 / 2)
        ky3 = dt * dy_dt(x + kx2 / 2, y + ky2 / 2, z + kz2 / 2)
        kz3 = dt * dz_dt(x + kx2 / 2, y + ky2 / 2, z + kz2 / 2)

        kx4 = dt * dx_dt(x + kx3, y + ky3, z + kz3)
        ky4 = dt * dy_dt(x + kx3, y + ky3, z + kz3)
        kz4 = dt * dz_dt(x + kx3, y + ky3, z + kz3)

        x2 = x + (kx1 + 2 * kx2 + 2 * kx3 + kx4) / 6
        y2 = y + (ky1 + 2 * ky2 + 2 * ky3 + ky4) / 6
        z2 = z + (kz1 + 2 * kz2 + 2 * kz3 + kz4) / 6

        j += 1

    i, j = 0, 0
    poinkare_section = [[], [], []]

    while j < 10000:
        x, y, z = x2, y2, z2

        kx1 = dt * dx_dt(x, y, z)
        ky1 = dt * dy_dt(x, y, z)
        kz1 = dt * dz_dt(x, y, z)

        kx2 = dt * dx_dt(x + kx1 / 2, y + ky1 / 2, z + kz1 / 2)
        ky2 = dt * dy_dt(x + kx1 / 2, y + ky1 / 2, z + kz1 / 2)
        kz2 = dt * dz_dt(x + kx1 / 2, y + ky1 / 2, z + kz1 / 2)

        kx3 = dt * dx_dt(x + kx2 / 2, y + ky2 / 2, z + kz2 / 2)
        ky3 = dt * dy_dt(x + kx2 / 2, y + ky2 / 2, z + kz2 / 2)
        kz3 = dt * dz_dt(x + kx2 / 2, y + ky2 / 2, z + kz2 / 2)

        kx4 = dt * dx_dt(x + kx3, y + ky3, z + kz3)
        ky4 = dt * dy_dt(x + kx3, y + ky3, z + kz3)
        kz4 = dt * dz_dt(x + kx3, y + ky3, z + kz3)

        x2 = x + (kx1 + 2 * kx2 + 2 * kx3 + kx4) / 6
        y2 = y + (ky1 + 2 * ky2 + 2 * ky3 + ky4) / 6
        z2 = z + (kz1 + 2 * kz2 + 2 * kz3 + kz4) / 6

        poinkare_section[0].append(x2)
        poinkare_section[1].append(y2)
        poinkare_section[2].append(z2)

        j += 1
    return poinkare_section

P = 0.4
mu = 0.1
c2 = 35.952
c3 = 534.43
w = 2

u0 = [0.1, 0.2, 0.3]

dt = 0.01
ps_z_b = runge_kutta(u0, dt)

syst = runge_kutta2(u0, dt)

plt.figure(figsize=(8, 6))
plt.scatter(ps_z_b[0], ps_z_b[1], color = 'k', s = 1)
plt.xlabel('X')
plt.ylabel('Y')

fig = plt.figure(figsize=(8, 6))

ax = fig.add_subplot(111, projection='3d')
ax.plot(syst[0], syst[1], syst[2], 'g.', ms=1, label='Фазовый портрет')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

plt.grid(True)

plt.show()