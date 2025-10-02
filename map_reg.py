import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams
from sys import stdout

rcParams['font.sans-serif']=['Arial', 'Dejavu Sans']
rcParams['font.size']=24
delta = 0.001
maxregim = 10 # максимально разрешимый режим
Ntrans = 10000


def Henon(x, A, B, C):
  dx = np.zeros(3)
  dx[0] = x[1]
  dx[1] = x[2]
  dx[2] = B*x[0] + A*x[2] + C*x[1] - x[1]**2
  return dx


plt.figure(figsize = (9, 9))

a_min = 1.42; a_d = 0.0002; a_max = 1.44
b = 0.5
c_min = -1.761; c_d = 0.00001; c_max = -1.759
a_n = np.arange(a_min, a_max+delta, a_d)
c_n = np.arange (c_min, c_max+delta, c_d)
map_Henon = np.zeros((len(a_n), len(c_n)), dtype=int)

for i, a in enumerate(a_n):
    stdout.write("\r%d" % i)
    stdout.flush()

    for j, c in enumerate(c_n):
        # stdout.write("\r%d" % j)
        # stdout.flush()

        #Пропускаем переходной процесс длины Ntrans
        x = [0.1, 0.1, 0.1] #начальные условия
        flag = False
        for n in range(Ntrans):
            x = Henon (x, a, b, c)
            if abs(x[0])>10:
              flag = True
              break
        if not flag:
            y_sec = [x[0]]
            for n in range(maxregim+1):
                x = Henon (x, a, b, c)
                y_sec.append(x[0])
            i_y = 1
            while i_y < len(y_sec) and abs(y_sec[i_y]-y_sec[0])>delta:
                i_y = i_y + 1
            if i_y > maxregim: i_y = maxregim
            map_Henon[i,j] = i_y

plt.imshow(map_Henon, cmap = 'jet', origin='lower',
           extent = (c_min, c_max, a_min, a_max), aspect = c_d / a_d)
plt.colorbar(boundaries=np.arange(-0.5, maxregim+1.5, 1),
             ticks=range(0, maxregim+1), fraction=0.044)

plt.xlabel(r'$\beta$', fontsize=28)
plt.ylabel(r'$\alpha$', fontsize=28)
plt.tight_layout()
# plt.savefig('map_Henon_1thread.png')
plt.show()
