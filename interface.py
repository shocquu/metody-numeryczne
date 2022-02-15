from scipy.optimize import root_scalar, bisect, newton as sp_newton
from mnum.nonlin_eq import bisection, newton, secant
from mnum.gauss import gauss_elimination
from numpy import tan, cos, exp, pi


''' Funkcje '''
def fwiki(x): return x**3 - x - 2   # bisection
def fwiki2(x): return x**2 - 612  # secant [10, 30], 5
def f1(x): return 1 if x == 0 else x**(-1) - tan(x)
def f2(x): return 2**(-x) + exp(x) + 2*cos(x) - 6
def f3(x): return 2*x**4 + 24*x**3 + 61*x**2 - 16*x + 1
def f3p(x): return 8*x**3 + 72*x**2 + 122*x - 16
def f4(x): return exp(x) - tan(x)
def f5(x): return x**3 - 12*x**2 + 3*x + 1


def printResult(result, comp):
    print('\n\x1b[6;30;42mWynik: {}, {} | blad: {}\x1b[0m'
          .format(result, comp, comp - result))


def cliInterface():
    print('''
    1. x^(-1) - tg(x)
    2. 2^(-x) + e^x + 2cos(x) - 6\'a
    3. 2x^4 + 24x^3 + 61x^2 - 16x + 1
    4. e^x - tg(x)
    5. x^3 - 12x^2 + 3x + 1

    Z Wikipedii:
    6. x^3 - x - 2
    7. x^2 - 612
    ''')
    func = int(input("Wybierz funkcje: "))
    print('''
    1. Metoda Bisekcji
    2. Metoda Newton\'a
    3. Metoda siecznych
    ''')
    method = int(input("Wybierz metode: "))

    # Funkcje
    if func == 1:
        f = f1
    elif func == 2:
        f = f2
    elif func == 3:
        f = f3
    elif func == 4:
        f = f4
    elif func == 5:
        f = f5
    elif func == 6:
        f = fwiki
    elif func == 7:
        f = fwiki2
    else:
        f = f1

    # Metody
    if method == 1:  # Bisekcja
        a, b = input("Wprowadz przedzial [a, b]: ").split(', ')
        a, b = [int(a), int(b)]
        tol = float(input("Wprowadz tolerancje (opcjonalne): ") or "0.0001")
        nmax = int(input("Wprowadz max iteracji (opcjonalne): ") or "20")
        inp = input("Wyswietlic tabele? [y/n] (opcjonalne): ")
        show = True if inp == "y" else False

        result = bisection(f, a, b, tol, nmax, show)
        scipy = bisect(f, a, b, xtol=tol)
        printResult(result, scipy)
    elif method == 2:  # Newton
        x0 = int(input("Wprowadz szacowana wartosc: ") or "1")
        result = newton(f, x0)
        scipy = sp_newton(f, x0)
        printResult(result, scipy)
    else:  # Sieczne
        x0, x1 = input("Wprowadz punkty poczatkowe [x0, x1]: ").split(', ')
        x0, x1 = [int(x0), int(x1)]
        nmax = int(input("Maksymalna liczba iteracji [<= 5]: ") or "5")

        result = secant(fwiki2, x0, x1, nmax)
        scipy = root_scalar(fwiki2, method='secant', x0=x0, x1=x1, maxiter=nmax).root
        printResult(result, scipy)


def main():
    a = [1, 0, 1]
    b = [2, pi/2, 3]
    ''' Metoda bisekcji '''
    result = bisection(fwiki, a[0], b[0], 0.0001, 15, True)
    # result = bisection(f1, a[1], b[1])
    scipy = bisect(fwiki, a[1], b[1], xtol=1e-4)

    ''' Metoda Newton'a '''
    # result = newton(fn, fnp, 1)
    # scipy = sp_newton(fn, 1, fnp)

    ''' Metoda siecznych '''
    # result = secant(fwiki2, 10, 30, 5)
    # scipy = root_scalar(fwiki2, method='secant', x0=10, x1=30, maxiter=5).root

    print('\n\x1b[6;30;42mWynik: {}, {} | blad: {}\x1b[0m'
          .format(result, scipy, scipy - result))


if __name__ == "__main__":
    main()
    # cliInterface()
    print('\033[96m=\033[0m'*49)
