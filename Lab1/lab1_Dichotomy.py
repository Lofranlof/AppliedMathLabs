import math as m

a = -5
b = 2.5
a = -100000
b = 1000000000
epsilon = 1e-7
alpha = epsilon / 2
steps = 1

def calcFunc(x):
    func = m.exp(m.sin(x))*m.pow(x, 2)
    #func = m.pow((x+1000), 2)
    return func

while (b - a) / 2 > epsilon:

    mid = (a + b) / 2
    c = mid - alpha
    d = mid + alpha
    
    if calcFunc(c) > calcFunc(d):
        a = c
    else:
        b = d
    steps += 1

print(mid)
print("Amount of steps", steps)