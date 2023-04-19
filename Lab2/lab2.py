from Derivatives import leftDer, rightDer, threePointsDer, threePointsDerLeft, threePointsDerRight
from Integrals import leftRectMethod, rightRectMethod, midRectMethod, SimpsonMethod, trapezoidMethod, calcFunc
import numpy as np
a = 0  # start of the interval
b = np.pi  # end of the interval

# a = 0
# b = 5

h = 0.1  # 1x accuracy
h = 0.05  # 2x accuracy
h = 0.025  # 4x accuracy
h = 0.0125  # 8x accuracy
h = 0.00625  # 16x accuracy

x = np.pi

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
