# quadratic formula ((x = -b +_ (b**2 - 4ac)**-2))/2a:
# discriminante(b**2 - 4ac)
import math

j = 1j


def quadratic(a, b, c):
    discriminant = (b**2) - 4(a)(c)
    hk = 0
    if discriminant < 0:
        hk = math.sqrt(math.abs(discriminant)) * j
    elif discriminant >= 0:
        hk = math.sqrt(discriminant)

    squareRoot = math.sqrt(discriminant)
    quadratic1 = (b + squareRoot)/2(a)
    quadratic2 = (b - squareRoot)/2(a)

    quad1 = str(quadratic1)
    quad2 = str(quadratic2)
    print(quad1 + " " + quad2)


quadratic(1, 2, 3)
