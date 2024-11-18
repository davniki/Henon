import numpy as np
import matplotlib.pyplot as plt

# Треугольник устойчивости динамической системы

b = 0.5

x0 = 0
y0 = 0
z0 = 0

a = np.linspace(-3, 3, 100)
a0 = np.linspace(0, 0, 100)
a1 = np.linspace(0.1, 0.1, 100)
a2 = np.linspace(0.15, 0.15, 100)
c0 = np.linspace(-2, 4, 100)

c1 = -b + 1 - a + 2 * y0
c2 = b + 1 + a + 2 * y0
c3 = -a * b + b ** 2 - 1 + 2 * y0

fig, ax = plt.subplots()
line1, = ax.plot(c1, a, label='Бифуркация+1')
line2, = ax.plot(c2, a, label='Бифуркция-1')
line3, = ax.plot(c3, a, label='Бифуркция-NS')
# line00, = ax.plot(c0, a0, label='A = 0')
# line01, = ax.plot(c0, a1, label='A = 0,1')
# line02, = ax.plot(c0, a2, label='A = 0,15')
A = ax.plot(-1.464, 1.43, 'ro')
where1 = (c1 >= c3) & (c1 <= c2)
where2 = (c2 >= c3) & (c2 <= c1)

ax.annotate('A=1.43, C=-1.464', xy=(-1.464, 1.43), xytext=(0, 2),
            arrowprops=dict(facecolor='black', shrink=0.05))
ax.legend(handles=[line1, line2, line3])
# line00, line01, line02])
ax.fill_betweenx(a, c1, c3, where=where1, color='lightyellow')
ax.fill_betweenx(a, c2, c3, where=where2, color='lightyellow')
ax.set_title(f'B = {b}')
ax.grid()
ax.set_xlabel('параметр C')
ax.set_ylabel('параметр A')

plt.show()
