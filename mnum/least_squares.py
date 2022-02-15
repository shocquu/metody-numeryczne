import numpy as np
import matplotlib.pyplot as plt
from mnum import gram_schmidt


class least_squares:
    def f1(self, x): return np.sin(-x) + np.exp(-x) - x**3
    def f2(self, x): return np.sin(x)
    def f3(self, x): return np.sqrt(x)
    def f4(self, x): return x**2 + 5*x + 6

    def orthogonalize(self, m):
        '''
        Testowa funkcja do ortogonalizacji wektorow na potrzeby
        zajec z aproksymacja sredniowkadratowa

        @arguments
            m : array
                tablica wektorow do zortogonalizowania

        @returns
            v : array
                zortogonalizowane wektory
        '''
        n = len(m)
        v = np.zeros((n, n))
        for j in range(n):
            v[j] = m[j]
            for i in range(j):
                u = np.dot(m[j], v[i])
                l = np.dot(v[i], v[i])
                v[j] -= u/l * v[i]
            v = v / np.absolute(np.sqrt(sum(v**2)))
        return v

    def getHilbertMatrix(self, n):
        '''
        Tworzy kwadratowa macierz Hiberta

        @url: https://en.wikipedia.org/wiki/Hilbert_matrix

        @arguments
            n : int
                wymiar macierzy

        @returns
            H : ndarray
                macierz Hiblerta o wymiarach NxN
        '''
        H = np.zeros((n + 1, n + 1))
        for i in range(n + 1):
            for j in range(n + 1):
                H[i, j] = 1 / ((i+1) + (j+1) - 0)

        return H

    def poly(self, coeff, x):
        '''
        Dla podanych wspolczynnikow zwraca wartosc argumentu x

        @arguments
            coeff : array
                tablica wspolczynnikow od stopnia n..0
            x : float
                wartosc, dla ktorej ma liczyc wielomian
        @returns
            c : float
                suma wspolczynnikow dla `x`
        '''
        n = len(coeff) - 1
        return sum(coeff[i]*x**(n-i) for i in range(len(coeff)))

    def plot(self, x, y, f, poly, a=-1, b=1):
        '''
        Dla podanego przedzialu <a, b> tworzy 50 rownoodleglych punktow,
        po czym rysuje przekazana funkcje oraz 2 wielomiany - odpowiednio
        obliczony uzywajac biblioteki NumPy oraz wlasny.

        @arguments
            f : func
                funkcja, ktora ma rysowac
            a : float
                dolny przedzial
            b : float
                gorny przedzial
        '''
        x_axis = np.linspace(a, b, 50)
        y_axis = f(x_axis)

        # plt.plot(x_axis, y_axis, '-r', label='funkcja')
        plt.plot(x, poly, '--g', label='wielomian')
        plt.ylabel('y')
        plt.xlabel('x')
        plt.scatter(x, y, marker="x")
        plt.title('Aproksymacja sredniokwadratowa')
        plt.legend(loc='upper right')
        plt.show()

    def linear(self, x, y):
        '''
        Dla przekazanych wspolrzednych tworzy funkcje liniowa
        bedaca aproksymacja zbioru punkow

        @arguments
            x : array
                tablica punktow dla osi X
            y : array
                tablica punktow dla osi Y

        @returns
            y : func
                funkcja liniowa y=ax+b
        '''
        n = len(x)
        Sxy = 0
        Sx2 = 0
        x_avg = sum(x) / n
        y_avg = sum(y) / n

        for i in range(n):
            Sxy += (x[i] - x_avg) * (y[i] - y_avg)
            Sx2 += (x[i] - x_avg)**2

        a = Sxy / Sx2
        b = y_avg - a*x_avg

        return a*x + b

    def quad_regression(self, x, y, n):
        '''
        Tworzy uklad rownan dla wielomianu stopnia `n`

        @arguments
            x : array
                wartosci na osi X
            y : array
                wartosci na osi Y
            n : int
                stopien wielomianu

        @returns
            a : array
                uklad rownan
            b : array
                wynik ukladu rownan
        '''
        n += 1
        m = len(x)
        a = np.zeros((n, n))
        b = np.zeros(n)
        for i in range(n):
            for j in range(n):
                k = n - (i + j) + 1
                a[i, j] = sum(x[xi]**k for xi in range(m))
            b[i] = sum(x[xi]**(n-i-1)*y[xi] for xi in range(m))
        a[i, j] = m
        return a, b

    def quad_regression2(self, x, y, n):
        n += 1
        a = np.zeros((n, n))
        b = np.zeros(n)
        for i in range(n):
            for j in range(n):
                k = (i + j) + 1
                a[i, j] = k
            b[i] = sum(x[xi]**(n-i-1)*y[xi] for xi in range(len(x)))
        a[0, 0] = n - 1
        print(a, b)
        return a, b

    def lst(self, x, f, w):
        return (f(x) - sum(w[i]*x**i for i in range(len(w)-1, -1, -1)))**2
