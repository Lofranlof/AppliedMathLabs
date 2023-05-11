import numpy as np
import random as rn
import matplotlib.pyplot as plt


def f(x, y):
    return x**2 + 2*y**2


def gradient_descent(step, num_iterations):
    # Начальные значения переменных
    x = np.array([5.0, 6.0])

    # Градиент функции
    def gradient(x):
        # Пример градиента для функции f(x, y) = x^2 + 2y^2
        grad = np.array([2 * x[0], 4 * x[1]])
        return grad

    # Итерационный процесс градиентного спуска
    x_history = []
    for i in range(num_iterations):
        x_history.append(x)
        grad = gradient(x)
        x = x - step * grad

    return x, x_history


# Параметры градиентного спуска
learning_rate = 0.1
iterations = 100

# Запуск градиентного спуска
result, history = gradient_descent(learning_rate, iterations)
print("Result: ", result)

# Создание сетки точек для отображения функции
x = np.linspace(-10, 10, 100)
y = np.linspace(-10, 10, 100)
X, Y = np.meshgrid(x, y)
Z = f(X, Y)

# Отображение функции
plt.contour(X, Y, Z, levels=20)
plt.scatter(result[0], result[1], color='red', label='Optimal Point')
plt.plot([point[0] for point in history], [point[1]
         for point in history], '-o', color='blue', label='Gradient Descent Path')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Function and Gradient Descent')
plt.show()
