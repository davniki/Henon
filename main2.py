import matplotlib.pyplot as plt
import numpy as np

x = 0.01
dx = 0.0001
sum = 0

fx = []
B = []
L = []

b = 0.001
m = 999
for j in range(2000):
    x0=x
    dx0=dx

    for i in range(300):
        x0 = b*x0*(1-x0**2)
        dx0 = b*(1 - 3*(x0**2))

    for i in range(m):
        x0 = b*x0*(1-x0**2)
        dx0 = b*(1 - 3*(x0**2))
        sum += np.log(abs(dx0))

    l = sum / m
    L.append(l)
    B.append(b)
    b += 0.001

plt.plot(B, L)
plt.show()
