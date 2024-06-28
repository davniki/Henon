import matplotlib.pyplot as plt
import numpy as np

a = 1.55
b = 0.7
c = -1.96

x0 = 0.1
y0 = 0.2
z0 = 0.3

x = 0
y = 0
z = 0

fx = []
fy = []
fz = []

r = []

n = 1000
m = 1000

for j in range(m):
    for i in range(n):
        z = (b * x0) + (a * z0) + (c * y0) - (y0 ** 2)
        x = y0
        y = z0

        z0 = z
        x0 = x
        y0 = y

    for i in range(n):
        z = b * x0 + a * z0 + c * y0 - y0 ** 2
        x = y0
        y = z0

        fz.append(z)
        fx.append(x)
        fy.append(y)
        r.append(c)

        z0 = z
        x0 = x
        y0 = y

    c += 0.00001


# ns1 = np.linspace(-1.59, -1.59, 100)
# ns2 = np.linspace(-1.89, -1.89, 100)
# ns4 = np.linspace(-1.953, -1.953, 100)
# ns3 = np.linspace(-1.941, -1.941, 100)
# ch = np.linspace(-1.954, -1.954, 100)

a = np.linspace(0.4, -1.2, 100)

fig, ax1 = plt.subplots()
ax1.plot(r, fx, 'r.', ms=0.01)
# line1, = ax1.plot(ns1, a, label='NS1')
# line2, = ax1.plot(ns2, a, label='NS2')
# line3, = ax1.plot(ns3, a, label='NS3')
# line4, = ax1.plot(ns4, a, label='NS4')
# line5, = ax1.plot(ch, a, label='CH')
# ax1.legend(handles=[line1, line2, line3, line4, line5])
ax1.set_title('A = 1,55; B = 0,7')
ax1.grid()
ax1.set_xlabel('параметр C')
ax1.set_ylabel('переменная X')

plt.show()
