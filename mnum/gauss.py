from numpy import zeros


def gauss_elimination2(a, b):
    n = len(b)

    for j in range(n - 1):
        for i in range(j + 1, n):
            if a[i][j] != 0:
                m = a[j][j] / a[i][j]

                for k in range(j, n):
                    a[i][k] = a[j][k] - a[i][k] * m

            b[i] = b[j] - b[i] * m


def gauss_elimination_test(a, b):
    n = len(b)

    for j in range(n - 1):
        for i in range(j + 1, n):
            if a[i][j] != 0:
                m = a[i][j] / a[j][j]

                for k in range(j, n - 1):
                    a[i][k] = a[i][j] - m * a[j][j]

            b[i] = b[j] - m * b[j]


def back_substitution2(a, b, x):
    n = len(b)
    x[n - 1] = b[n - 1] / a[n - 1][n - 1]

    for i in range(n - 2, -1, -1):
        sum_ax = 0

        for j in range(i+1, n):
            sum_ax += a[i][j] * x[j]

        x[i] = (b[i] - sum_ax) / a[i][i]


def gauss_crout_old(a, b):
    n = len(b)
    l = zeros((n, n))
    u = zeros((n, n))

    for k in range(n):
        l[k][k] = a[k][k] - sum(l[k][s] * u[s][k] for s in range(k - 1))

        for j in range(k, n):
            sum_lu = sum(l[k][s] * u[s][j] for s in range(k + 1))
            u[k][j] = (a[k][j] - sum_lu) / l[k][k]

        for i in range(k + 1, n):
            sum_lu = sum(l[i][s] * u[s][k] for s in range(k + 1))
            l[i][k] = (a[i][k] - sum_lu) / u[k][k]

    return l, u

# ======================== #


def gauss_elimination(a, b):
    '''
    Rozwiazuje rownania liniowe

    @arguments
        a : ndarray
            macierz wspolczynnikow
        b : array
            macierz wynikow

    @returns
    '''
    n = len(b)

    for j in range(n - 1):
        for i in range(j + 1, n):
            m = 1
            if a[i][j] != 0:
                m = a[i][j] / a[j][j]

                for k in range(j, n):
                    a[i][k] -= m * a[j][k]

            b[i] -= m * b[j]

    return (a, b)


def back_substitution(a, b):
    n = len(b)
    x = zeros(n)

    for i in range(n - 1, -1, -1):
        x[i] = b[i]

        for j in range(i + 1, n):
            x[i] -= a[i][j] * x[j]

        x[i] /= a[i][i]

    return x


def gauss_crout(a, b):
    '''
    Tworzy macierz dolna L i gorna U

    @parameters
        a : 2darray
        b : array
    @returns
        L : ndarray
            dolna macierz L
        U : ndarray
            gorna macierz U
    '''
    n = len(b)
    l = zeros((n, n))
    u = zeros((n, n))

    for j in range(n):
        u[j][j] = 1

        for i in range(n):
            sum_lu = sum(l[i][s] * u[s][j] for s in range(1, j - 1))
            l[j][i] = (a[j][i] - sum_lu)  # / u[k][k]

        for i in range(j, n):
            sum_lu = sum(l[j][s] * u[s][i] for s in range(1, j - 1))
            u[i][j] = (a[i][j] - sum_lu) / l[j][j]

    return l, u
