import matplotlib.pyplot as plt
import numpy as np
from mpmath import mp

mp.dps = 10


class Henon():
    def __init__(self, x, a, b, c):
        self.x = x
        self.a = a
        self.b = b
        self.c = c

    def iteration(self):
        dx = mp.matrix([[0, 0, 0]])
        dx[0] = self.x[1]
        dx[1] = self.x[2]
        dx[2] = self.b * self.x[0] + self.a * self.x[2] + self.c * self.x[1] - self.x[1] ** 2
        self.x[0] = dx[0]
        self.x[1] = dx[1]
        self.x[2] = dx[2]

    def bif_tree(self, step, trans_iter, iter, step_prm):
        # The bifurcation tree
        fx = []
        fy = []
        fz = []
        r = []
        for j in range(step):
            for i in range(trans_iter):
                self.iteration()
            for i in range(iter):
                self.iteration()
                fx.append(self.x[0])
                fy.append(self.x[1])
                fz.append(self.x[2])
                r.append(self.c)
            self.c += step_prm

        fig, ax = plt.subplots()
        ax.plot(r, fx, 'r.', ms=0.02)
        ax.grid()
        ax.legend()
        ax.set_title(f'Бифуркационное дерево системы с параметрами A = {self.a}, B = {self.b}')
        ax.set_xlabel('Параметр C')
        ax.set_ylabel('X')
        plt.show()

    def triangle(self):
        # Треугольник устойчивости динамической системы

        a = np.linspace(-3, 3, 100)

        c1 = -self.b + 1 - a + 2 * self.x[1]
        c2 = self.b + 1 + a + 2 * self.x[1]
        c3 = -a * self.b + self.b ** 2 - 1 + 2 * self.x[1]

        fig, ax = plt.subplots()
        line1, = ax.plot(c1, a, label='Бифуркация+1')
        line2, = ax.plot(c2, a, label='Бифуркация-1')
        line3, = ax.plot(c3, a, label='Бифуркация-NS')

        # where1 = (c1 >= c3) & (c1 <= c2)
        # where2 = (c2 >= c3) & (c2 <= c1)

        ax.legend(handles=[line1, line2, line3])
        # ax.fill_betweenx(a, c1, c3, where=where1, color='lightyellow')
        # ax.fill_betweenx(a, c2, c3, where=where2, color='lightyellow')
        ax.set_title(f'B = {self.b}')
        ax.grid()
        ax.set_xlabel('параметр C')
        ax.set_ylabel('параметр A')

        plt.show()

    def fase_port(self, n, m):
        fx = []
        fy = []
        fz = []

        for i in range(m):
            self.iteration()

        for i in range(n):
            self.iteration()
            fx.append(self.x[0])
            fy.append(self.x[1])
            fz.append(self.x[2])

        fig, ax = plt.subplots()
        ax.plot(fx, fy, 'g.', ms=0.09)
        ax.set_title(f'A = {self.a}, B = {self.b}, C = {self.c}')
        ax.grid()
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        plt.show()

    def close_fase_port(self, n, m, x_start, x_end, y_start, y_end):
        fx1 = []
        fy1 = []
        fz1 = []

        for i in range(m):
            self.iteration()

        for i in range(n):
            self.iteration()
            if x_start < self.x[0] < x_end and y_start < self.x[1] < y_end:
                fx1.append(self.x[0])
                fy1.append(self.x[1])
                fz1.append(self.x[2])

        fig, ax1 = plt.subplots()
        ax1.plot(fx1, fy1, 'g.', ms=0.09)
        ax1.set_title(f'A = {self.a}, B = {self.b}, C = {self.c}')
        ax1.grid()
        ax1.set_xlabel('X')
        ax1.set_ylabel('Y')
        plt.show()


ds = Henon(
    mp.matrix([[mp.mpf('0.1'), mp.mpf('0.2'), mp.mpf('0.3')]]),
    mp.mpf('1.43'),
    mp.mpf('0.5'),
    mp.mpf('-1.7594137')
)

# print(ds.x)
# for i in range(10_000):
#     ds.iteration()
#
# print(ds.x)

ds.bif_tree(1000, 1000, 1000, 0.0004)
# ds.triangle()
# ds.fase_port(300_000, 10_000)
# ds.close_fase_port(300000, 100000, -0.46, -0.18, -0.63, -0.23)
