import matplotlib.pyplot as plt
from mpmath import mp

mp.dps = 10

# Метод Руннге-Кутты 4-го порядка для оного уравнения

# dx/dt = f(x, t)
# x_0 = x(t_0)

# k_1 = f(x_n, t_n)
# k_2 = f(x_n + (dt/2)*k_1, t_n