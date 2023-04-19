from Derivatives import leftDer, rightDer, threePointsDer, threePointsDerLeft, threePointsDerRight
from Integrals import leftRectMethod, rightRectMethod, midRectMethod, SimpsonMethod, trapezoidMethod, calcFunc

a = 0  # start of the interval
b = 5  # end of the interval
h = 0.0001  # step
n = (b - a) / h  # number of points
x = 3

if __name__ == '__main__':
    print("Derivative stuff: \n")
    print("Evaluated function at given point x:", calcFunc(x))
    print("Left derivative at given point x:", leftDer(x, h))
    print("Right derivative at given point x:", rightDer(x, h))
    print("Three points derivative at given point x:", threePointsDer(x, h))
    print("Three points derivative at the right boundary:",
          threePointsDerRight(b, h))
    print("Three points derivative at the left boundary:",
          threePointsDerLeft(a, h))

    print("Integral stuff: \n")
    print("Integral of the function from a to b using left rectangle method:", leftRectMethod(x, h))
    print("Integral of the function from a to b using right rectangle method:", rightRectMethod(x, h))
    print("Integral of the function from a to b using midpoint method:", midRectMethod(x, h))
    print("Integral of the function from a to b with Simpson's rule:", SimpsonMethod(x, h))
    print("Integral of the function from a to b with Trapezoidal rule:", trapezoidMethod(x, h))
