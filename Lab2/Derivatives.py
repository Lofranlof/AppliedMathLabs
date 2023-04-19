from Function import calcFunc

def rightDer(x, h):
    return (calcFunc(x+h) - calcFunc(x)) / h


def leftDer(x, h):
    return (calcFunc(x) - calcFunc(x-h)) / h


def threePointsDer(x, h):
    return (calcFunc(x+h)-calcFunc(x-h)) / (2 * h)


def threePointsDerLeft(a, h):
    return (-3 * calcFunc(a) + 4 * calcFunc(a+h) - calcFunc(a+2*h)) / (2 * h)


def threePointsDerRight(b, h):
    return (calcFunc(b - h*2) - 4 * calcFunc(b - h) + 3 * calcFunc(b)) / (2 * h)
