from numpy import zeros, array


class doolittle:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.n = len(b)
        self.x = zeros(self.n)

    def decomposition(self, show=False):
        l = zeros((self.n, self.n))
        u = zeros((self.n, self.n))

        for k in range(self.n):
            l[k][k] = 1

            for j in range(k, self.n):
                sum_lu = sum(l[k][s] * u[s][j] for s in range(k))
                u[k][j] = (self.a[k][j] - sum_lu)

            for i in range(k + 1, self.n):
                sum_lu = sum(l[i][s] * u[s][k] for s in range(k))
                l[i][k] = (self.a[i][k] - sum_lu) / u[k][k]

        print('{} \n {}'.format(array(l), array(u)) if show == True else '')
        return (l, u)

    def forward_substitution(self, l):
        y = zeros(self.n)
        y[0] = self.b[0] / l[0][0]

        for i in range(1, self.n):
            sum_ly = sum(l[i][j] * y[j] for j in range(i))
            y[i] = (self.b[i] - sum_ly) / l[i][i]

        return y

    def back_substitution(self, u, y):
        self.x[self.n - 1] = y[self.n - 1] / u[self.n - 1][self.n - 1]

        for i in range(self.n - 1, -1, -1):
            sum_ux = sum(u[i][j] * self.x[j] for j in range(i + 1, self.n))
            self.x[i] = (y[i] - sum_ux) / u[i][i]

        return self.x

    def cholesky2(self):
        l = zeros((self.n, self.n))

        for k in range(self.n):
            sum_l = sum(l[k][s]**2 for s in range(k - 2))
            l[k][k] = (self.a[k][k] - sum_l)**(1/2)

            for i in range(k, self.n):
                sum_ll = sum(l[i][s] * l[k][s] for s in range(k - 2))
                l[i][k] = (self.a[i][k] - sum_ll) / l[k][k]

        return l

    def cholesky(self):
        l = zeros((self.n, self.n))

        for i in range(self.n):
            for j in range(i + 1):
                sum_l = sum(l[i][s] * l[j][s] for s in range(j))

                if (i == j):
                    l[i][j] = (self.a[i][i] - sum_l)**(1/2)
                else:
                    l[i][j] = (self.a[i][j] - sum_l) / l[j][j]

        return l
