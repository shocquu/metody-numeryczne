from scipy.misc import derivative


def bisection(f, a, b, tol=1e-4, nmax=15, show=False):
    if f(a) < 0 and f(b) < 0:
        return

    n = 1
    if show:
        print('\x1b[6;30;42m{:<4}{:<16}{:<16}{:<18}{:<25}\x1b[0m'.format('It', 'an', 'bn', 'cn', 'f(c)'))

    while(n <= nmax):
        c = (a + b) / 2

        if f(c) == 0 or (b - a) / 2 < tol:
            return c
        if show:
            print('{:<4}{:<16}{:<16}{:<18}{:<16}'.format(n, a, b, c, f(c)))

        a, b = (c, b) if f(c) * f(a) > 0 else (a, c)
        n += 1

    return -1


def newton(f, x0, fp=None, tol=1e-7, eps=1e-14, nmax=20, show=False):
    found = False

    if show:
        print('\x1b[6;30;42m{:<4}{:<16}{:<16}{:<18}\x1b[0m'.format('n', 'x', 'accuracy', 'f(x)'))
    for n in range(1, nmax):
        y = f(x0)
        # yp = fp(x0)
        yp = derivative(f, x0)

        if abs(yp) < eps:
            break
        x1 = x0 - y/yp
        if abs(x1 - x0) < tol:
            found = True
            break
        if show:
            print('{:<4}{:<16}{:<16}{:<18}'.format(n, x0, x1, f(x0)))
        x0 = x1

    if found:
        return x1
    return -1


def secant(f, x0, x1, nmax=5):
    for _ in range(nmax):
        result = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        x0, x1 = x1, result
    return result
