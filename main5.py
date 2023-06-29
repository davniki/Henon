import matplotlib.pyplot as plt
import numpy as np

plt.style.use('_mpl-gallery')

# Make data
a = 1.55
b = 0.7
c = -1.941

x0 = 0.1
y0 = 0.2
z0 = 0.3

x = 0
y = 0
z = 0

fx = []
fy = []
fz = []

n = 10000

for i in range(n):
    z = b * x0 + a * z0 + c * y0 - y0 ** 2
    x = y0
    y = z0

    z0 = z
    x0 = x
    y0 = y

for i in range(n):
    z = b * x0 + a * z0 + c * y0 - y0 ** 2
    x = y0
    y = z0

    z0 = z
    x0 = x
    y0 = y

    fz.append(z0)
    fx.append(x0)
    fy.append(y0)

# Plot
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
ax.scatter(fx, fy, fz, marker=".")

plt.show()
