import numpy as np


class newton_cotes:
    '''
    Zbior metod do cwiczen 'Całkowanie numeryczne'

    @parameters
        a : int
            przedzial poczatkowy calkowania
        b : int
            przedzial koncowy calkowania
        n : int = (10)
            zalozona dokladnosc
    '''

    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.n = 10

    '''
    Wykorzystane podczas zajec funkcje

    @parameters
        x : float
            polozenie na osi X
    '''

    def f1(self, x): return x**2 * pow(np.sin(x), 3)
    def f2(self, x): return np.exp(x**2) * (x - 1)

    def f3(self, x):
        a = 55
        b = -2
        c = -6
        d = 5
        e = 0.4

        return e*(x**4) + d*(x**3) + c*(x**2) + b*x + a

    def f4(self, x):
        a = 1
        b = -2
        c = -6

        return a + b*np.exp(x) + c*np.cos(x)

    def trapezoidal(self, f, n):
        '''
        Regula trapezoidalna
            @url: https://en.wikipedia.org/wiki/Trapezoidal_rule

            @parameters
                f : func
                    calkowana funkcja
                n : int
                    ilosc punktow

            @returns
                _ : float
                    wynik calkowania
        '''
        h = (self.b - self.a) / n
        sum_xi = sum(f(self.a + i*h) for i in range(n))
        return h/2 * (f(self.a) + 2*sum_xi + f(self.b))

    def simpson(self, f, n):
        '''
        Regula Simpson'a 1/3. Wersja z uwzglednieniem parzystosci indeksu.
            @url: https://en.wikipedia.org/wiki/Simpson%27s_rule#Simpson's_1/3_rule

            @parameters
                f : func
                    calkowana funkcja
                n : int
                    ilosc punktow

            @returns
                _ : float
                    wynik calkowania
        '''
        h = (self.b - self.a) / n
        result = f(self.a) + f(self.b)

        for i in range(1, n):
            xi = self.a + i*h

            if i % 2 != 0:
                result += 4 * f(xi)
            else:
                result += 2 * f(xi)

        return h/3 * result

    def gauss_legendre_5p(self, f):
        '''
        Przyklad algorytmu Gauss-Legendre'a 5P z dolaczonej ksiazki

        @parameters
            f : fun
                calkowana funkcja

        @returns
            _ : float
                wynik calkowania dla przedzialu <a, b>
                odczytanego z parametrow klasy
        '''
        x = [0.1488743389816312, 0.4333953941292472, 0.6794095682990244, 0.8650633666889845, 0.9739065285171717]
        w = [0.2955242247147529, 0.2692667193099963, 0.2190863625159821, 0.1494513491505806, 0.0666713443086881]

        xm = 0.5 * (self.b + self.a)
        xr = 0.5 * (self.b - self.a)
        s = 0

        for i in range(5):
            dx = xr * x[i]
            s += w[i] * (f(xm+dx) + f(xm-dx))

        return s * xr

    def gauss_legendre_4p(self, f, n=4):
        '''
        Kwadratura Gauss-Legendre'a dla n <= 4 z uwzglednieniem zmiany
        przedzialu calkowania

        @parameters
            f : fun
                calkowana funkcja
            n : int = 4
                liczba punktow do oczytu z tablicy
                punktow i wag `x`, `A`

        @returns
            _ : float
                wynik calkowania dla przedzialu <a, b>
                odczytanego z parametrow klasy
        '''
        x = [[-0.577350, 0.577350],
             [-0.774597, 0, 0.774597],
             [-0.861136, -0.339981, 0.339981, 0.861136],
             [-0.906180, -0.538469, 0, 0.538469, 0.906180],
             ]
        A = [[1, 1],
             [0.555556, 0.888889, 0.555556],
             [0.347855, 0.6521445, 0.6521445, 0.347855],
             [0.236927, 0.478629, 0.568889, 0.478629, 0.236927]
             ]

        hm = (self.b - self.a) / 2
        hp = (self.b + self.a) / 2

        return hm * sum(A[n-1][i] * f(hm * x[n - 1][i] + hp) for i in range(n + 1))

    def gauss_leg_4p(self, f, n=4):
        '''
        Kwadratura Gauss-Legendre'a dla n <= 4 bez uwzglednienia zmiany
        przedzialu calkowania. Oczekiwany wynik dla przedzialu <-1, 1>,
        niezgodnosci dla innych przedzialow

        @parameters
            f : fun
                calkowana funkcja
            n : int = 4
                liczba punktow do oczytu z tablicy
                punktow i wag `x`, `A`

        @returns
            _ : float
                wynik calkowania dla przedzialu <a, b>
                odczytanego z parametrow klasy
        '''
        x = [[-0.577350, 0.577350],
             [-0.774597, 0, 0.774597],
             [-0.861136, -0.339981, 0.339981, 0.861136],
             [-0.906180, -0.538469, 0, 0.538469, 0.906180],
             ]
        A = [[1, 1],
             [5/9, 8/9, 5/9],
             [0.347855, 0.6521445, 0.6521445, 0.347855],
             [0.236927, 0.478629, 0.568889, 0.478629, 0.236927]
             ]

        return sum(A[n-1][i] * f(x[n - 1][i]) for i in range(n + 1))
