import numpy as np
func = 'np.power(x, 3)'
# func = 'np.sin(x)'


def calcFunc(x):
    def function(x): return eval(func)
    return function(x)
