def lagrange_interpolation(Lx, x, y):
    '''
    Zwraca interpolowana wartosc

    @parameters
        Px : int
            punkt interpolacyjny
        x : array<float>
            wspolrzedne na osi X
        y : array<float>
            wspolrzedne na osi X

    @returns
        Py : float
            interpolowana wartosc

    '''
    Ly = 0

    for i in range(len(x)):
        l = 1

        for j in range(len(x)):
            if j != i:
                l *= (Lx - x[j]) / (x[i] - x[j])
        Ly += l * y[i]

    return Ly
