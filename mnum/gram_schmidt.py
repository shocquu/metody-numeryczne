import numpy as np


class gram_schmidt:
    def __init__(self, A):
        '''
        Klasa do zajec o tematyce `Gram-Schmidt`

        @parameters
            A : 2Darray<float>
        '''
        self.A = np.array(A).T
        self.n = len(A)
        self.v = np.zeros((self.n, self.n))
        self.w = np.zeros((self.n, self.n))

    def transpose(self, m):
        '''
        Dokonuje transpozycji macierzy
            @parameters
                m : 2Darray<float>
                    macierz do operacji

            @returns
                m : 2Darray<float>
                    przetransponowana macierz
        '''
        return ((m[x][y] for x in range(len(m))) for y in range(len(m[0])))

    def vdot(self, a, b):
        '''
        Iloczyn skalarny dwoch macierzy
            @parameters
                a : 2Darray<float>
                    macierz do operacji
                b : 2Darray<float>
                    macierz do operacji

            @returns
                _ : float
                    wynik mnożenia
        '''
        return sum(x * y for x, y in zip(a, b))

    def normalize(self, v):
        '''
        Proces normalizacji bazy
            @parameters
                v : array<float>
                    baza ortogonalna

            @returns
                _ : array<float>
                    baza ortonormalna
        '''
        return v / np.absolute(np.sqrt(sum(v**2)))

    def orthogonalize(self):
        '''
        Proces ortogonalizacji Grama-Schmidta. Zrobiony z mysla
        o tematyce zajec. Nie uwzglednia macierzy o wymiarach innych
        niz 3x3.

            @attributes
                A : 2Darray<float>
                    macierz odczytana z atrybutu klasy

            @returns
                v : array<float>
                    zortogonalizowana macierz / wektor
        '''
        for j in range(self.n):
            self.v[j] = self.A[j]

            for i in range(j):
                u = np.vdot(self.A[j], self.v[i])
                l = np.vdot(self.v[i], self.v[i])
                self.v[j] -= u/l * self.v[i]

            self.w[j] = self.normalize(self.v[j])

        return self.v

    def qr_decomposition(self):
        '''
        Kompozycja QR. Operacje na kolumnach dokonane sa
        poprzez transpozycje operowanej macierzy.
            @url: https://en.wikipedia.org/wiki/QR_decomposition
            @returns
                self.w.T : 2Darray<float>
                    macierz ortonormalna Q
                R : 2Darray<float>
                    macierz diagonalna gorna R
        '''
        R = np.zeros((self.n, self.n))
        self.v = self.orthogonalize()

        for j in range(self.n):
            for i in range(j, self.n):
                R[j, i] = np.vdot(self.w[j], self.A[i])

        return self.w.T, R

    ''' Regula trojczlonowa WIP '''
    # def Pk(self, x, alfa, beta, gamma):
    #     return (alfa*x + beta) * Pk(x) + gamma*Pk(x)

    # def Pn(x): return a[n, n]*Pn(x) + a[n-1, n] * P(x) + a[n+1, n]*
    def P(self, x, p, k):
        alfa = np.zeros((k, k))
        for j in range(k + 1):
            alfa[k, j] = np.dot(x*p[k], p[j]) / np.absolute(p[j] ** 2)

    def troj(self):
        p = np.zeros(self.n)
        x = self.orthogonalize()

        for k in range(self.n):
            p[k] = self.P(x, p, k)

        # p[0] = 1

        for i in range(1, self.n):
            p[i] = 2**i * sum(np.vdot(2**i, p[k])/np.vdot(p[k], p[k]) * p[k] for k in range(i - 1))

        print(p)

    def trojczlon(self):
        P = np.zeros(self.n)
        P[0] = 0
        P[1] = self.A[0, 0]

        for k in range(self.n):
            alfa = self.a[k]/self.a[k-1]
            beta = -1
