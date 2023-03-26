import math as m

a = -5.0
b = 2.5

a = -1000
b = 1000
epsilon = 1e-7
steps = 1

def calcFunc(x):
    func = m.exp(m.sin(x)) * m.pow(x, 2)
    #func = m.pow((x-20), 2)
    return func

GOLD_RATIO = (3.0 - m.sqrt(5.0)) / 2.0

# Initialize variables
v = w = x = a + GOLD_RATIO * (b - a)
fv = fw = fx = calcFunc(x)
d = e = b - a
eps2 = 2.0 * epsilon

while True:

    mid = 0.5 * (a + b)

    if abs(mid - x) <= eps2:
        print((x + mid) / 2)
        print(steps)
        exit()

    # Fit parabola
    if abs(e) > epsilon:
        
        r = (x - w) * (calcFunc(x) - calcFunc(v))
        q = (x - v) * (calcFunc(x) - calcFunc(w))
        p = (x - v) * q - (x - w) * r
        q = 2 * (q - r)

        if q > 0.0:
            p = -p
        else:
            q = -q

        r = e
        e = d

        if abs(p) < abs(0.5 * q * r):
            # SPI step
            d = p / q
            u = x + d
            # f must not be evaluated too close to a or b
            if u - a < eps2 or b - u < eps2:
                if x < mid:
                    d = epsilon
                else:
                    d = -epsilon
        else:
            # GSS step
            if x < mid:
                e = b - x
            else:
                e = a - x

            d = GOLD_RATIO * e

    # f must not be evaluated too close to x
    if abs(d) >= epsilon:
        u = x + d
    elif d > 0:
        u = x + epsilon
    else:
        u = x - epsilon

    fu = calcFunc(u)

    if fu <= fx:
        if u >= x:
            a = x
        else:
            b = x

        v = w
        fv = fw
        w = x
        fw = fx
        x = u
        fx = fu
    else:
        if u < x:
            a = u
        else:
            b = u

        if fu <= fw or w == x:
            v = w
            fv = fw
            w = u
            fw = fu
        elif fu <= fv or v == x or v == w:
            v = u
            fv = fu

    steps += 1




    