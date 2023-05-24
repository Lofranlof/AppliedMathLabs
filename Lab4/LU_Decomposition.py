import numpy as np


def lu_decomposition(A):
    n = len(A)
    L = np.eye(n)
    U = np.zeros((n, n))

    for k in range(n):
        U[k, k:] = A[k, k:] - L[k, :k] @ U[:k, k:]
        L[(k + 1):, k] = (A[(k + 1):, k] - L[(k + 1):, :k] @ U[:k, k]) / U[k, k]

    return L, U


def forward_substitution(L, b):
    n = len(L)
    y = np.zeros(n)

    for i in range(n):
        y[i] = (b[i] - L[i, :i] @ y[:i]) / L[i, i]

    return y


def backward_substitution(U, y):
    n = len(U)
    x = np.zeros(n)

    for i in range(n - 1, -1, -1):
        x[i] = (y[i] - U[i, (i + 1):] @ x[(i + 1):]) / U[i, i]

    return x


def solve_lu(A, b):
    L, U = lu_decomposition(A)
    y = forward_substitution(L, b)
    x = backward_substitution(U, y)
    return x


# Example usage:
A = np.array([[1, 1, 3], [0, 1, 3], [-1, 3, 0]])
b = np.array([[1], [3], [5]])

x = solve_lu(A, b)
print("Solution:", x)
