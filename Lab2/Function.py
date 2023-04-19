func = 'x**3'

def calcFunc(x):
    def function(x): return eval(func)
    return function(x)
