import matplotlib.pyplot as plt

a = 1.43
b = 0.5
c = -1.8

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
        r.append(c)

    c += 0.001

fig, ax1 = plt.subplots()
ax1.plot(r, fx, 'r.', ms=0.01);

fig, ax2 = plt.subplots()
ax2.plot(fy, fx, 'g.', ms=0.01);

plt.show()
