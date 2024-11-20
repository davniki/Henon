import numpy as np


def Henon(x, A, B, C):
    # dx = np.array([0, 0, 0])
    x0 = x[1]
    x1 = x[2]
    x2 = B * x[0] + A * x[2] + C * x[1] - x[1] ** 2

    return np.array([x0, x1, x2])


x = np.array([0.01, 0.01, 0.01])

A = -0.227
B = -0.5
C = -1.375

L1 = 0
L2 = 0
L3 = 0

for i in range(100):
    x = Henon(x, A, B, C)

eps = 0.001
x0 = np.array([x[0] + eps, x[1], x[2]])
x1 = np.array([x[0], x[1] + eps, x[2]])
x2 = np.array([x[0], x[1], x[2] + eps])

for i in range(300):
    x = Henon(x, A, B, C)

    x0 = Henon(x0, A, B, C)
    x1 = Henon(x1, A, B, C)
    x2 = Henon(x2, A, B, C)
    # print(x0, x)
    d0 = x0 - x
    d1 = x1 - x
    d2 = x2 - x

    # norm = sqrt(x0[0]^2 - x[0]^2, x0[1]^2 - x[1]^2, x0[2]^2 - x[2]^2)
    norm1 = np.linalg.norm(d0)
    norm2 = np.linalg.norm(d1)
    norm3 = np.linalg.norm(d2)
    # print(norm)
    L1 = L1 + np.log(norm1/eps)
    L2 = L2 + np.log(norm2/eps)
    L3 = L3 + np.log(norm3/eps)

    d0 = d0 / norm1

    d_1 = d1 - (d1 @ d0.T) * d0
    norm_2 = np.linalg.norm(d_1)
    d1 = d_1 / norm_2

    d_2 = d2 - (d2 @ d0.T) * d0 - (d2 @ d1.T) * d1
    norm_3 = np.linalg.norm(d_2)
    d2 = (d_2 / norm_3) * eps
    d1 = d1 * eps
    d0 = d0 * eps
    # print(d0 @ d1.T, d1 @ d2.T, d0 @ d2.T)
    # print()

    x0 = x + d0
    x1 = x + d1
    x2 = x + d2

L_end1 = L1 / 300
L_end2 = L2 / 300
L_end3 = L3 / 300

print(L_end1, L_end2, L_end3)
