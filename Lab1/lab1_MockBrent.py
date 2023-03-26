import math as m
from scipy.optimize import minimize_scalar

def calcFunc(x):
    func = m.exp(m.sin(x)) * m.pow(x, 2)
    #func = m.pow((x-20), 2)
    return func

res = minimize_scalar(calcFunc)
print(res)
