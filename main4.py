import matplotlib.pyplot as plt

a = 1.55
b = 0.7
c=-1.95366

x0 = 0.1
y0 = 0.2
z0 = 0.3

x = 0
y = 0
z = 0

fx = []
fy = []
fz = []

n = 100000

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

fig, ax = plt.subplots()
ax.plot(fx, fy, 'g.', ms=0.15)

ax.set_title('C = -1,95366')
ax.grid()
ax.set_xlabel('X')
ax.set_ylabel('Y')

plt.show()
