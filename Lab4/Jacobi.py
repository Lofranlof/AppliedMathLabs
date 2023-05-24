import math
import copy
 
def exitCondition(x_old, x_new):
    eps = 0.0001
    sum_up = 0
    sum_low = 0
    for k in range(0, len(x_old)):
        sum_up += (x_new[k] - x_old[k]) ** 2
        sum_low += (x_new[k]) ** 2
 
    return math.sqrt(sum_up / sum_low) < eps
 
 
def solution(a, b):
 
    amount_of_x = len(b)
 
    x_k = [1 for k in range(0, amount_of_x)]
 
    number_of_iter = 0
 
    while 1:
 
        x_before_k = copy.deepcopy(x_k)
 
        for i in range(0, amount_of_x):
           S = 0
           for j in range(0, amount_of_x):
                if j != i:
                    S = S + a[i][j] * x_k[j]
           x_k[i] = b[i] / a[i][i] - S / a[i][i]
 
        if exitCondition(x_before_k, x_k):
            break
 
        number_of_iter += 1
 
    print('Amount of iterations: ', number_of_iter)
 
    return x_k
 
 
# Ответ к примеру:  x = [1.10202, 0.99091, 1.01111]
 
a = [[10, 1, -1],
     [1, 10, -1],
     [-1, 1, 10]]
 
b = [11, 10, 10]
 
print('Solution: ', solution(a, b))