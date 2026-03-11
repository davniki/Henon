import mpmath as mp


def henon(x, a, b, c):
    dx = mp.matrix([[0, 0, 0]])
    dx[0] = x[1]
    dx[1] = x[2]
    dx[2] = b * x[0] + a * x[2] + c * x[1] - x[1] ** 2
    return dx


def d_henon(dx, x, a, b, c):
    dx0 = mp.matrix([[0, 0, 0]])
    dx0[0] = dx[1]
    dx0[1] = dx[2]
    dx0[2] = b * dx[0] + (c - 2 * x[1]) * dx[1] + a * dx[2]
    return dx0


def lyp_exp(x, a, b, c):
# начальные вектора возмущения, которые ортоганальны и нормированы на еденицу
    dx = mp.matrix([[mp.mpf('1'), 0, 0]])
    dy = mp.matrix([[0, mp.mpf('1'), 0]])
    dz = mp.matrix([[0, 0, mp.mpf('1')]])

    m = 2000
    t = 20

    l_1 = 0
    l_2 = 0
    l_3 = 0

    sum_1 = 0
    sum_2 = 0
    sum_3 = 0

    g_1 = 0
    g_2 = 0
    g_3 = 0

    for l in range(1000):
        x = henon(x, a, b, c)

    for j in range(m):
        for i in range(t):
            x = henon(x, a, b, c)
            dx = d_henon(dx, x, a, b, c)
            dy = d_henon(dy, x, a, b, c)
            dz = d_henon(dz, x, a, b, c)

        if mp.norm(dx, 2) != 0:
            sum_1 += mp.log(mp.norm(dx, 2))
            g_1 += 1
            dx = dx / mp.norm(dx, 2)

        dy1 = dy - (dy * dx.T)[0] * dx
        if mp.norm(dy1, 2) != 0:
            sum_2 += mp.log(mp.norm(dy1, 2))
            g_2 += 1
            dy = dy1 / mp.norm(dy1, 2)

        dz1 = dz - (dz * dx.T)[0] * dx - (dz * dy.T)[0] * dy
        if mp.norm(dz1, 2) != 0:
            sum_3 += mp.log(mp.norm(dz1, 2))
            g_3 += 1
            dz = dz1 / mp.norm(dz1, 2)

    l_1 = sum_1 / (g_1 * t)
    l_2 = sum_2 / (g_2 * t)
    l_3 = sum_3 / (g_3 * t)

    return l_1, l_2, l_3