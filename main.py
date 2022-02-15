import matplotlib.pyplot as plt
import scipy as sp
import numpy as np
import mnum


def chart(a, b, n, f):
    ''' Wykresy '''
    ax = plt.axes()

    x = np.linspace(a, b, 100)
    y = f(x)
    ax.plot(x, y, 'o')

    xstep = np.linspace(a, b, n)
    ax.fill_between(xstep, f(xstep), 0, color='tab:olive')
    plt.show()


def main():
    ''' Gauss '''
    # a = [[1, 2, 1, -1], [3, 2, 4, 4], [4, 4, 3, 4], [2, 0, 1, 5]]
    # b = [5, 16, 22, 15]
    # a, b = mnum.gauss_elimination(a, b)
    # x = mnum.back_substitution(a, b)
    # print(x)

    ''' Crout '''
    # l, u = mnum.gauss_crout(a, b)
    # print('Crout:\nL:\n{} \n\n U:\n{}'.format(np.array(l), np.array(u)))

    ''' Interpolacje '''
    # x = [-2, -1, 0, 1, 2]
    # y = [5, -2, 4, -7, 2]
    # Ly = mnum.lagrange_interpolation(4, x, y)
    # Ny = mnum.newton_interpolation(4, x, y)
    # print('Lagrange: {}\nNewton: {}\n'.format(Ly, Ny))

    ''' Doolittle '''
    # doolittle = mnum.doolittle(a, b)
    # l, u = doolittle.decomposition()
    # y = doolittle.forward_substitution(l)
    # x = doolittle.back_substitution(u, y)
    # print('Doolittle:\n L:\n{} \n\n U:\n{}'.format(np.array(l), np.array(u)))

    ''' Cholesky '''
    # l = doolittle.cholesky()
    # print('Cholesky:\n L:\n{}'.format(array(l)))
    # l = np.linalg.cholesky(array(a))
    # print('Numpy:\n L:\n{}'.format(array(l)))

    ''' Kwadratury'''
    # a = 0
    # b = 4.5
    # n = 10_000
    # nc = mnum.newton_cotes(a, b)
    # f = nc.f1
    # # chart(a, b, 4, f)
    # print('  Wzór trapezów:{0:.>31f}'.format(nc.trapezoidal(f, n)))
    # print('  Wzór Simpson\'a:{0:.>30f}'.format(nc.simpson(f, n)))
    # print('  Wzór Gaussa-Legendre\'a (5):{0:.>18f}'.format(nc.gauss_legendre_5p(f)))
    # print('  Wzór Gaussa-Legendre\'a (4):{0:.>18f}'.format(nc.gauss_legendre_4p(f)))
    # print('  Wzór Gaussa-Legendre\'a (4 | NC):{0:.>13f}'.format(nc.gauss_leg_4p(f)))

    ''' Gram-Schmidt '''
    # A = [[1, 2, 2], [-1, 0, 2], [0, 0, 1]]
    # A = [[1, 2, 4], [0, 0, 5], [0, 3, 6]]
    # A = [[1, 1, 0], [1, 0, 1], [0, 1, 1]]
    # A = [[12, -51, 4], [6, 167, -68], [-4, 24, -41]]
    # gs = mnum.gram_schmidt(A)
    # u = gs.orthogonalize()
    # Q, R = gs.qr_decomposition()

    # print('u:\n{}\ne:\n{}'.format(u.T, gs.w.T))
    # print('Q:\n{}\nR:\n{}'.format(Q, R))

    ''' Aproksymacje '''
    ls = mnum.least_squares()
    a = -1
    b = 1
    n = 2

    ''' Polyval & Polyfit '''
    # x = np.linspace(a, b, 5)
    # y = ls.f1(x)
    # H = ap.getHilbertMatrix(n)
    # coeff = np.polyfit(x, ap.f1(x), n)
    # poly1 = np.polyval(coeff, x)
    # poly2 = ap.poly(coeff, x)
    # ap.plot(x, y, ap.f1, poly2, a, b)

    x1 = np.array([-3, -2, -1, 0, 1, 2, 3])
    y1 = np.array([7.5, 3, 0.5, 1, 3, 6, 14])

    a1, b1 = ls.quad_regression(x1, y1, n)
    print(a1, '\n{:-^20s}\n'.format(''), b1, '\n')

    a2, b2 = mnum.gauss_elimination(a1, b1)
    xgauss = mnum.back_substitution(a2, b2)
    npgauss = np.linalg.solve(a1, b1)
    polyfit = np.polyfit(x1, y1, n)

    # print(sum(x1**2*y1))
    print('Gauss:\t\t{}\nGauss Numpy:\t{}\nPolyfit:\t{}'.format(xgauss, npgauss, polyfit))

    poly3 = ls.poly(polyfit, x1)
    poly4 = ls.poly(xgauss, x1)
    ls.plot(x1, y1, ls.f1, poly3, -3, 3)

    ''' Wykres '''
    # plt.plot(x1, y1, '-r', label='funkcja')
    # plt.plot(x1, poly3, '--g', label='wielomian')
    # plt.plot(x1, poly4, '--b', label='wielomian')
    # plt.ylabel('y')
    # plt.xlabel('x')
    # plt.scatter(x1, y1, marker="x")
    # plt.title('Aproksymacja sredniokwadratowa')
    # plt.legend(loc='upper right')
    # plt.show()


if __name__ == "__main__":
    main()
    print('\033[96m=\033[0m'*49)
