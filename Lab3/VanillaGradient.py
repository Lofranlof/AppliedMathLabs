import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

plt.rcParams["figure.figsize"] = (20, 15)
mpl.rcParams["axes.unicode_minus"] = False

def func1(x, y):
    return np.cos(x) + y ** 2

def df1_x(x, y):
    return -np.sin(x)

def df1_y(x, y):
    return 2 * y

def func2(x, y):
    return x ** 2 + y ** 2 - x * y

def df2_x(x, y):
    return 2 * x - y

def df2_y(x, y):
    return 2 * y - x

def func3(x, y):
    return x ** 2 + 1/2 * y ** 2 - y * x + 4 * y

def df3_x(x, y):
    return 2 * x - y

def df3_y(x, y):
    return y - x + 4

def makeGraph(title, a, b, f, x_list, y_list):
    X = np.arange(a, b, 0.1)
    Y = np.arange(a, b, 0.1)
    X, Y = np.meshgrid(X, Y)
    Z = np.array([X.ravel(), Y.ravel()]).T
    Z = f(Z[:, 0], Z[:, 1])
    Z = Z.reshape(X.shape)

    m = plt.contour(X, Y, Z, 40)
    plt.title(title)
    plt.colorbar(m)
    plt.plot(x_list, y_list, 'o-', c="purple")
    plt.show()

def vanillaGradient(title, f, df_x, df_y,  x0, y0, eps, alpha, a, b):
    x_list, y_list = [], []

    x_list.append(x0)
    y_list.append(y0)

    last_x, last_y = x0, y0
    curr_x = last_x - alpha * df_x(last_x, last_y)
    curr_y = last_y - alpha * df_y(last_x, last_y)
    counter = 1
    while(abs(f(curr_x, curr_y)-f(last_x, last_y)) > eps):
        x_list.append(curr_x)
        y_list.append(curr_y)

        last_x, last_y = curr_x, curr_y
        curr_x = last_x - alpha * df_x(last_x, last_y)
        curr_y = last_y - alpha * df_y(last_x, last_y)
        counter += 1

    title = title + "\nConst Step"
    makeGraph(title, a, b, f, x_list, y_list)

    print("Constant step gradient descent")
    print("Number of iterations:", counter)
    print("x:", curr_x)
    print("y:", curr_y, "\n")

title = "Function: cos(x) + y^2"
print(title)
vanillaGradient(title, func1, df1_x, df1_y, 2, 4, 0.00001, 0.3, -5, 5)

title = "Function: x^2 + y^2 - xy"
print(title)
vanillaGradient(title, func2, df2_x, df2_y, 5, 8, 0.00001, 0.3, -10, 10)

title = "Function:  x^2 + 1/2*y^2 - yx + 4y"
print(title)
vanillaGradient(title, func3, df3_x, df3_y, -15, 15, 0.00001, 0.5, -18, 18)