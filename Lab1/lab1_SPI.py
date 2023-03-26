import math as m
import numpy as np

def calcFunc(x):
    func = m.exp(m.sin(x)) * m.pow(x, 2)
    #func = m.pow((x + 100), 2)
    #func = (m.pow(x + 10, 2))
    return func



def calcU(x1, x2, x3):
    coefficientArray = np.array([[m.pow(x1, 2), x1, 1], [m.pow(x2, 2), x2, 1], [m.pow(x3, 2), x3, 1]])
    vectorArray = np.array([calcFunc(x1), calcFunc(x2), calcFunc(x3)])
    result = np.linalg.solve(coefficientArray, vectorArray)
    return -result[1] / (2 * result[0])

x1 = -2.5
x3 = 5
x2 = (x1 + x3) / 2

epsilon = 1e-7
steps = 1
while True:
    u = calcU(x1, x2, x3)
    if abs(x2 - u) <= epsilon:
        print((x2 + u) / 2)
        print(steps)
        break
    elif calcFunc(x3) > calcFunc(x1):
        if u < x2:
            x3 = x2
            x2 = u
        else:
            x3 = u
    elif calcFunc(x1) > calcFunc(x3):
        if u < x2:
            x1 = u
        else:
            x1 = x2
            x2 = u
    steps += 1
