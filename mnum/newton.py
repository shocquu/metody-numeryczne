def newton_interpolation(Nx, x, y):
    '''
    Zwraca interpolowana wartosc

    @parameters
        Nx : int
            punkt interpolacyjny
        x : array<float>
            wspolrzedne na osi X
        y : array<float>
            wspolrzedne na osi X

    @returns
        Ny : float
            interpolowana wartosc
    '''
    n = len(x)
    a = [[None for i in range(n)] for j in range(n)]
    yi = [None for i in range(n)]

    for i in range(n):
        a[i][0] = y[i]

    for j in range(1, n):
        for i in range(n - j):
            a[i][j] = (a[i + 1][j - 1] - a[i][j - 1]) / (x[i + j] - x[i])

    Ny = 0
    m = 1
    yi[0] = a[0][0]  # y0 = f(x0)

    for i in range(1, n):
        m *= Nx - x[i - 1]
        yi[i] = yi[i - 1] + a[0][i] * m
        Ny = yi[i]

    return Ny
