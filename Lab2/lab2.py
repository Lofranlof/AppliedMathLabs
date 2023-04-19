from Derivatives import leftDer, rightDer, threePointsDer, threePointsDerLeft, threePointsDerRight
from Integrals import leftRectMethod, rightRectMethod, midRectMethod, SimpsonMethod, trapezoidMethod, calcFunc

a = 0  # start of the interval
b = 5  # end of the interval
h = 0.0001  # step
n = (b - a) / h  # number of points
x = 3

if __name__ == '__main__':
    print("Function's value at the given point x:", calcFunc(x), '\n')
    print("Derivative stuff: \n")
    print("Left derivative at given point x:", leftDer(x, h))
    print("Right derivative at given point x:", rightDer(x, h))
    print("Three points derivative at given point x:", threePointsDer(x, h))
    print("Three points derivative at the right boundary:",
          threePointsDerRight(b, h))
    print("Three points derivative at the left boundary:",
          threePointsDerLeft(a, h), "\n")

    print("Integral stuff: \n")
    print("Integral of the function from a to b using left rectangle method:",
          leftRectMethod(a, b, h))
    print("Integral of the function from a to b using right rectangle method:",
          rightRectMethod(a, b, h))
    print("Integral of the function from a to b using midpoint method:",
          midRectMethod(a, b, h))
    print("Integral of the function from a to b with Simpson's rule:",
          SimpsonMethod(a, b, h))
    print("Integral of the function from a to b with Trapezoidal rule:",
          trapezoidMethod(a, b, h))
