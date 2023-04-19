from Function import calcFunc

def leftRectMethod(a, b, h):
    sum = 0
    x = a
    while x < b:
        sum += h * calcFunc(x - h)
        x += h
    return sum

def rightRectMethod(a, b, h):
    sum = 0
    x = a
    while x < b:
        sum += h * calcFunc(x + h)
        x += h
    return sum


def midRectMethod(a, b, h):
    sum = 0
    x = a
    while x < b:
        sum += h * calcFunc(x - h / 2)
        x += h
    return sum


def trapezoidMethod(a, b, h):
    sum = 0
    x = a
    while x < b:
        sum += (h / 2) * (calcFunc(x - h) + calcFunc(x))
        x += h
    return sum

def SimpsonMethod(a, b, h):
    sum = 0
    x = a
    while x < b:
        sum += (h / 6) * (calcFunc(x - h) + 4 * calcFunc(x - h / 2) + calcFunc(x))
        x += h
    return sum