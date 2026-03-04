import matplotlib.pyplot as plt
import numpy as np
from Lyp_exp2 import lyp_exp
from sys import stdout

delta = 0.01

a_min = 1.67
a_max = 2
a_d = (a_max - a_min) / 100
a_n = np.arange(a_min, a_max + delta, a_d)

b = 0.5

c_min = -1.91
c_max = -1.83
c_d = (c_max - c_min) / 100
c_n = np.arange(c_min, c_max + delta, c_d)

map_Henon = np.zeros((len(a_n), len(c_n)))

for i, a in enumerate(a_n):
    stdout.write("\r%d" % i)
    stdout.flush()

    for j, c in enumerate(c_n):
        # начальные условия
        x = np.array([0.1, 0.1, 0.1])

        lexp = lyp_exp(x, a, b, c)

        if lexp[0] < -0.001 and lexp[1] < -0.001 and lexp[2] < -0.001:
            map_Henon[i, j] = 0

        elif (-0.001 < lexp[0] < 0.001) and lexp[1] < -0.001 and lexp[2] < -0.001:
            map_Henon[i, j] = 1

        elif (-0.001 < lexp[0] < 0.001) and (-0.001 < lexp[1] < 0.001) and lexp[2] < -0.001:
            map_Henon[i, j] = 2

        elif lexp[0] > 0.001 and lexp[1] < -0.001 and lexp[2] < -0.001:
            map_Henon[i, j] = 3

        elif lexp[0] > 0.001 and (-0.001 < lexp[1] < 0.001) and lexp[2] < -0.001:
            map_Henon[i, j] = 4

        elif lexp[0] > 0.001 and lexp[1] > 0.001 and lexp[2] < -0.001:
            map_Henon[i, j] = 5

        else:
            map_Henon[i, j] = 6

print(map_Henon)

plt.imshow(
    map_Henon.T,
    cmap = 'jet',
    origin = 'lower',
    extent = (a_min, a_max, c_min, c_max),
    aspect = a_d / c_d
)

plt.title(f'Карта Ляпуновских показатлей B = {b}')
plt.xlabel("Параметр A")
plt.ylabel("Параметр C")

plt.colorbar()
plt.show()


