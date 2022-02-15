from .lagrange import lagrange_interpolation
from .newton import newton_interpolation
from .gauss import gauss_elimination, back_substitution, gauss_crout
from .nonlin_eq import bisection, newton, secant
from .doolittle import doolittle
from .quadratures import newton_cotes
from .gram_schmidt import gram_schmidt
from .least_squares import least_squares

print(('\033[96m{:=^49s}\033[0m').format(' Metody Numeryczne '))
