import matplotlib.pyplot as plt
# import numpy as np
from sys import stdout
from mpmath import mp
from models import lyp_exp

mp.dps = 30
# Спектр ляпуновских показателей


# def Henon(x, A, B, C):
#     dx = mp.matrix([[0, 0, 0]])
#     dx[0] = x[1]
#     dx[1] = x[2]
#     dx[2] = B * x[0] + A * x[2] + C * x[1] - x[1] ** 2
#     return dx
#
#
# def d_Henon(dx, x, A, B, C):
#     dx0 = mp.matrix([[0, 0, 0]])
#     dx0[0] = dx[1]
#     dx0[1] = dx[2]
#     dx0[2] = B * dx[0] + (C - 2 * x[1]) * dx[1] + A * dx[2]
#     return dx0


A = mp.mpf('1.43')
B = mp.mpf('0.5')

C_min = mp.mpf('-1.761')
C_max = mp.mpf('-1.758')
delta = abs(C_max - C_min)/100

C = mp.arange(C_min, C_max, delta)

m = 2000
t = 20

L_1 = []
L_2 = []
L_3 = []
Parametr_C = []

for q, c in enumerate(C):
    stdout.write("\r%d" % q)
    stdout.flush()

    x = mp.matrix([[mp.mpf('0.1'), mp.mpf('0.1'), mp.mpf('0.1')]])

    l1, l2, l3 = lyp_exp(x, A, B, c)

    L_1.append(l1)
    L_2.append(l2)
    # L_3.append(l3)
    Parametr_C.append(c)

# fp1 = np.linspace(-1.464, -1.464, 100) # NS
# fp2 = np.linspace(2.1175, 2.1175, 100)
# fp3 = np.linspace(2.035, 2.035, 100)
# fp4 = np.linspace(2.0031, 2.0031, 100)
#
# fp5 = np.linspace(1.99362, 1.99362, 100)
# fp6 = np.linspace(1.99148, 1.99148, 100)
# fp7 = np.linspace(1.991006, 1.991006, 100)
# fp8 = np.linspace(-1.619, -1.619, 100) # HC

fig, ax = plt.subplots()

# a1 = np.linspace(-0.002, 0.002, 100)

l1 = ax.plot(Parametr_C, L_1, label='L-1')
l2 = ax.plot(Parametr_C, L_2, label='L-2')
# l3 = ax.plot(Parametr_C, L_3, label='L-3')

# line1, = ax.plot(fp1, a1, label='NS')
# line2, = ax.plot(fp2, a1, label='ICD-1')
# line3, = ax.plot(fp3, a1, label='ICD-2')
# line4, = ax.plot(fp4, a1, label='ICD-3')
#
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