import math as m

a = -5.0
b = 2.5
epsilon = 1e-7
steps = 1

def calcFunc(x):
    func = m.exp(m.sin(x))*m.pow(x, 2)
    #func = m.pow((x-1000), 2)
    return func

def Fib(n):
    x = 0
    y = 1
    while n > 1:
        z = x + y
        x = y
        y = z
        n -= 1
    return x + y

def calcSteps(epsilon, a, b):
    Fn = (b - a) / epsilon
    n = 0
    while Fn >= Fib(n):
        n += 1
    return n

n = calcSteps(epsilon, a, b)

def calcX1(a, b):
    return a + (Fib(n - 2) / Fib(n) * (b - a))

def calcX2(a, b):
    return a + (Fib(n - 1) / Fib(n) * (b - a))

x1 = calcX1(a, b)
x2 = calcX2(a, b)

fx1 = calcFunc(x1)
fx2 = calcFunc(x2)

while n > 0:
 
    if fx1 > fx2:
        a = x1
        x1 = x2
        fx1 = fx2
        x2 = calcX2(a, b)
        fx2 = calcFunc(x2)

    elif fx1 <= fx2:
        b = x2
        x2 = x1
        fx2 = fx1
        x1 = calcX1(a, b)
        fx1 = calcFunc(x1)

    n -= 1
    steps += 1

print((b + a) / 2)
print(steps)