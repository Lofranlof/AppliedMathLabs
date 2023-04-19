import numpy as np
#func = 'x**3'
func = 'np.sin(x)'
def calcFunc(x):
    def function(x): return eval(func)
    return function(x)
