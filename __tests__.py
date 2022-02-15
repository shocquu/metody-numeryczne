import pytest
import mnum

a4 = [[0, -3, 4, 6.8, 9], [-3, 2, 4.6, 6.3, -10], [2, -1, 2.8, -8.4, -5], [-6, 2, 7, -0.5, -0.9], [5, -2, -0.5, 12, -4]]  # [0, 0, -3.23, -66.33, -434.53],
b4 = [66.64, -36.26, -4.32, 16.6, -12.9]

a3 = [[1, 2, 1, -1], [3, 2, 4, 4], [4, 4, 3, 4], [2, 0, 1, 5]]
b3 = [5, 16, 22, 15]

a2 = [[6, -2, 2, 4], [12, -8, 6, 10], [3, -13, 9, 3], [-6, 4, 1, -18]]
b2 = [12, 34, 27, -38]

a1 = [[4, -2, 4, -2], [3, 1, 4, 2], [2, 4, 2, 1], [2, -2, 4, 2]]
b1 = [8, 7, 10, 2]

x = [0, 0, 0, 0]


def test_1():
    mnum.gauss_elimination(a1, b1)
    mnum.back_substitution(a1, b1, x)
    assert x == pytest.approx([-1., 2., 3., -2.])


def test_2():
    mnum.gauss_elimination(a2, b2)
    mnum.back_substitution(a2, b2, x)
    assert x == pytest.approx([1., -3., -2., 1.])


def test_3():
    mnum.gauss_elimination(a3, b3)
    mnum.back_substitution(a3, b3, x)
    assert x == pytest.approx([16., -6., -2., -3.])

# def test_4():
#     mnum.gauss_elimination(a4, b4)
#     mnum.back_substitution(a4, b4, x)
#     assert x == pytest.approx([2., -1., 5., -0.2, 5.])


# def test_x():
#     mnum.gauss_elimination(a1, b1)
#     mnum.back_substitution(a1, b1, x)

#     assert x == pytest.approx(numpy.multiply(a1, x))
