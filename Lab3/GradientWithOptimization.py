import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from VanillaGradient import makeGraph
from VanillaGradient import func1, func2, func3, df1_x, df1_y, df2_x, df2_y, df3_x, df3_y


plt.rcParams["figure.figsize"] = (20, 15)
mpl.rcParams["axes.unicode_minus"] = False

def golden_ratio(a, b, eps, x, y, f, df_x, df_y):
    phi = (1 + 5 ** 0.5) / 2
    l1 = b - (b - a)/phi
    l2 = a + (b - a)/phi
    f1 = f(x-l1*df_x(x,y), y-l1*df_y(x,y))
    f2 = f(x-l2*df_x(x,y), y-l2*df_y(x,y))
    while (b - a) > eps:
        if f1 < f2:
            b, l2, f2 = l2, l1, f1
            l1 = b - (b - a)/phi
            f1 = f(x-l1*df_x(x,y), y-l1*df_y(x,y))
        else:
            a, l1, f1 = l1, l2, f2
            l2 = a + (b - a)/phi
            f2 = f(x-l2*df_x(x,y), y-l2*df_y(x,y))

    return (a + b) / 2


def grad_down_gold(title, f, df_x, df_y,  x0, y0, eps, a, b):
    x_list, y_list = [], []

    x_list.append(x0)
    y_list.append(y0)

    last_x, last_y = x0, y0
    alpha = golden_ratio(a, b, eps, last_x, last_y, f, df_x, df_y)
    curr_x = last_x - alpha * df_x(last_x, last_y)
    curr_y = last_y - alpha * df_y(last_x, last_y)
    counter = 1
    while abs(f(curr_x, curr_y)-f(last_x, last_y)) > eps:
        x_list.append(curr_x)
        y_list.append(curr_y)

        last_x, last_y = curr_x, curr_y
        alpha = golden_ratio(a, b, eps, last_x, last_y, f, df_x, df_y)
        curr_x = last_x - alpha * df_x(last_x, last_y)
        curr_y = last_y - alpha * df_y(last_x, last_y)
        counter += 1

    title = title + "\nGold"
    makeGraph(title, a, b, f, x_list, y_list)

    print("Gradient descent with golden ratio")
    print("Number of iterations:", counter)
    print("x:", curr_x)
    print("y:", curr_y, "\n")

    
title = "Function: cos(x) + y^2"
print(title)
grad_down_gold(title, func1, df1_x, df1_y, 2, 4, 0.00001, -5, 5)

title = "Function: x^2 + y^2 - xy"
print(title)
grad_down_gold(title, func2, df2_x, df2_y, 5, 8, 0.00001, -10, 10)

title = "Function:  x^2 + 1/2*y^2 - yx + 4y"
print(title)
grad_down_gold(title, func3, df3_x, df3_y, -15, 15, 0.00001, -18, 18)
