import matplotlib.pyplot as plt
import numpy as np
from sys import stdout
from Lyp_exp2 import lyp_exp


# Спектр ляпуновских показателей


a_min = 1.97561
a_max = 1.97564
a_d = (a_max - a_min)/100

A = np.arange(a_min, a_max, a_d)
B = 0.5
C = -1.9

L_1 = []
L_2 = []
L_3 = []
par = []


for i, a in enumerate(A):
    stdout.write("\r%d" % i)
    stdout.flush()

    x = np.array([0.1, 0.1, 0.1])

    l1, l2, l3 = lyp_exp(x, a, B, C)

    L_1.append(l1)
    L_2.append(l2)
    # L_3.append(l3)
    par.append(a)

# fp1 = np.linspace(-1.464, -1.464, 100) # NS
# fp2 = np.linspace(2.1175, 2.1175, 100)
# fp3 = np.linspace(2.035, 2.035, 100)
# fp4 = np.linspace(2.0031, 2.0031, 100)
# fp5 = np.linspace(1.99362, 1.99362, 100)
# fp6 = np.linspace(1.99148, 1.99148, 100)
# fp7 = np.linspace(1.991006, 1.991006, 100)
# fp8 = np.linspace(-1.619, -1.619, 100) # HC

fig, ax = plt.subplots()

# a1 = np.linspace(-0.002, 0.002, 100)

l1 = ax.plot(par, L_1, label='L-1')
l2 = ax.plot(par, L_2, label='L-2')
# l3 = ax.plot(c, L_3, label='L-3')

# line1, = ax.plot(fp1, a1, label='NS')
# line2, = ax.plot(fp2, a1, label='ICD-1')
# line3, = ax.plot(fp3, a1, label='ICD-2')
# line4, = ax.plot(fp4, a1, label='ICD-3')
# line5, = ax.plot(fp5, a1, label='ICD-4')
# line6, = ax.plot(fp6, a1, label='ICD-5')
# line7, = ax.plot(fp7, a1, label='ICD-6')
# line8, = ax.plot(fp8, a1, label='HC')

# ax.annotate('NS', xy=(-1.47, 0), xytext=(-1.42, 0.1),
#             arrowprops=dict(facecolor='black', shrink=0.05))
# ax.annotate('ICD-1', xy=(2.1175, 0), xytext=(2.15, 0.025),
#             arrowprops=dict(facecolor='black', shrink=0.05))
# ax.annotate('ICD-2', xy=(2.035, 0), xytext=(2.075, 0.025),
#             arrowprops=dict(facecolor='black', shrink=0.05))
# ax.annotate('ICD-3', xy=(2.0031, 0), xytext=(2.005, 0.003),
#             arrowprops=dict(facecolor='black', shrink=0.05))
# ax.annotate('ICD-4', xy=(1.99362, 0), xytext=(1.9975, 0.003),
#             arrowprops=dict(facecolor='black', shrink=0.05))
# ax.annotate('ICD-5', xy=(1.99148, 0), xytext=(1.9925, 0.003),
#             arrowprops=dict(facecolor='black', shrink=0.05))
# ax.annotate('ICD-6', xy=(1.991006, 0), xytext=(1.991025, 0.0005),
#             arrowprops=dict(facecolor='black', shrink=0.05))
# ax.annotate('ICD-2', xy=(-1.759255, 0), xytext=(-1.725, 0.066),
#             arrowprops=dict(facecolor='black', shrink=0.05))


ax.grid()
ax.legend()
# ax.legend(handles=[line1, line2, line3, line4])
ax.set_title(f"C = {C}, B = {B}")
ax.set_xlabel("Параметр A")
ax.set_ylabel("Показатель Ляпунова L")

plt.show()