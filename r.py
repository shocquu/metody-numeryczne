import numpy as np
import matplotlib.pyplot as plt


def euler_method(f, y0, t, h=1, show=False):
    n = len(t)
    y = np.zeros(n)
    y[0] = f(t[0], y0)
    print('\x1b[6;30;42m{:<4}{:<4}{:<4}{:<10}{:<4}{:<6}{:<4}\x1b[0m'.format('n', 'yn', 'tn', 'f(tn, yn)', 'h', '\u0394y', 'yn+1')) if show else 0
    for i in range(n-1):
        y[i+1] = y[i] + h * f(t[0], y[i])
        print(f'{i:<4}{y[i]:<4}{t[i]:<4}{f(y[i]):<10}{h:<4}{y[i+1]-y[i]:<6}{y[i+1]:<4}') if show else 0
    return y


def heuns_method(f, y0, t, h=1):
    n = len(t)
    y = np.zeros(n)
    y[0] = y0

    for i in range(n-1):
        in_y = y[i] + h*f(t[i], y[i])
        y[i+1] = y[i] + h/2*(f(t[i], y[i]) + f(t[i] + h, in_y))
    return y


def midpoint_method(f, y0, t, h=1, method='explicit'):
    n = len(t)
    y = np.zeros(n)
    y[0] = y0

    if method == 'implicit':
        for i in range(n-1):
            y[i+1] = y[i] + h*f(t[i] + h/2, 0.5*(y[i] + y[i+1]))
        return y

    for i in range(n-1):
        y[i+1] = y[i] + h*f(t[i] + h/2, y[i] + h/2*f(t[i], y[i]))
    return y


def runge_kuta_method(f, y0, t, h=1):
    n = len(t)
    y = np.zeros(n)
    y[0] = y0
    for i in range(n-1):
        k1 = f(t[i], y[i])
        k2 = f(t[i] + h/2, y[i] + h*k1/2)
        k3 = f(t[i] + h/2, y[i] + h*k2/2)
        k4 = f(t[i] + h, y[i] + h*k3)
        y[i+1] = y[i] + h/6 * (k1 + 2*k2 + 2*k3 + k4)
        t[i+1] = t[i] + h
    return y


# Do zrobienia
def crank_nicolson(y):
    return y


def f(t, y): return y
def T(t, y, alfa=14e-6, beta=42e-6): return alfa*(t**4 - beta)


def dt(t, y=1, ro=1, R=1, sigma=1, T0=1): return 7/9*ro*R/(np.e*sigma*T0**3)


def main():
    # ===== KULA =====
    # a = 0
    # b = 350
    # y0 = 1200
    # h = 1
    # func = T
    # t = np.linspace(a, 350, 100)
    # exact = T(t, 1)
    # ================

    a = 0
    b = 4
    y0 = 1
    h = 0.25
    func = f

    t = np.arange(a, b+1, h)
    exact = np.exp(t)
    euler = euler_method(func, y0, t, h)
    heun = heuns_method(func, y0, t, h)
    mide = midpoint_method(func, y0, t, h)
    midi = midpoint_method(func, y0, t, h, method='implicit')
    kuta = runge_kuta_method(func, y0, t, h)

    # test = [dt(ti) for ti in t]
    # print(test)

    # print(t)
    # print(f'Dokladne:\t{exact}\nEuler:\t\t{euler}\nHeun:\t\t{heun}\nMidpoint(imp):\t{midi}\nMidpoint(exp):\t{mide}\nRunge-Kuta:\t{kuta}')

    # plt.plot(t, lambda t: 14e-6*(t**4 - 42e-6), 'r-')
    plt.plot(t, exact, 'r-')
    plt.plot(t, euler, 'b.-')
    plt.plot(t, heun, 'g.-')
    plt.plot(t, mide, 'y.--')
    plt.plot(t, midi, 'm.-')
    plt.plot(t, kuta, 'c.--')
    plt.legend([
        'Dokladne',
        'Euler',
        'Heun',
        'Midpoint(imp)',
        'Midpoint(exp)',
        'Runge-Kuta'
    ])
    plt.xticks(t)
    plt.grid()
    plt.show()


if __name__ == "__main__":
    main()
    print('\033[96m=\033[0m'*49)
