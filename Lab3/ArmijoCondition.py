import numpy as np


def f(x, y):
    return x**2 + 2*y**2


def gradient(x):
    # Пример градиента для функции f(x, y) = x^2 + 2y^2
    grad = np.array([2 * x[0], 4 * x[1]])
    return grad


def armijo_line_search(x, grad, func, alpha=0.1, beta=0.5):
    t = 0.1
    while func(x - t * grad) > func(x) - alpha * t * np.linalg.norm(grad)**2:
        t *= beta
    return t


def gradient_descent_armijo(stepSize, num_iterations, func, grad_func):
    # Начальные значения переменных
    x = np.array([5.0, 6.0])

    # Итерационный процесс градиентного спуска
    for i in range(num_iterations):
        grad = grad_func(x)
        t = armijo_line_search(x, grad, func)
        x = x - t * grad

    return x


# Параметры градиентного спуска
stepSize = 1.0
iterations = 100

# Запуск градиентного спуска с условием Армихо
result = gradient_descent_armijo(stepSize, iterations, f, gradient)
print("Result: ", result)
