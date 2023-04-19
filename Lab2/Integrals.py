from Function import calcFunc

def leftRectMethod(x, h):
    return h * calcFunc(x - h)


def rightRectMethod(x, h):
    return h * calcFunc(x + h)


def midRectMethod(x, h):
    return h * calcFunc(x - h / 2)


def trapezoidMethod(x, h):
    return (h / 2) * (calcFunc(x - h) + calcFunc(x))

def SimpsonMethod(x, h):
    return (h / 6) * (calcFunc(x - h) + 4 * calcFunc(x - h / 2) + calcFunc(x))