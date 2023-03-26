import math as m

a = -5.0
b = 2.5

a = -100000
b = 100000000
epsilon = 1e-7
steps = 1
gRatio = (m.sqrt(5) - 1) / 2

def calcFunc(x):
    func = m.exp(m.sin(x)) * m.pow(x, 2)
    #func = m.pow((x+10), 2)
    return func

def calcDistance(a, b):
    return gRatio * (b - a)

x1 = b - calcDistance(a, b)
x2 = a + calcDistance(a, b)

fx1 = calcFunc(x1)
fx2 = calcFunc(x2)

while b - a > epsilon:
 
    if fx1 > fx2:
        a = x1
        x1 = x2
        fx1 = fx2
        x2 = a + calcDistance(a, b)
        fx2 = calcFunc(x2)

    elif fx1 <= fx2:
        b = x2
        x2 = x1
        fx2 = fx1
        x1 = b - calcDistance(a, b)
        fx1 = calcFunc(x1)

    steps += 1

print ((b + a) / 2)
print("Amount of steps", steps)

