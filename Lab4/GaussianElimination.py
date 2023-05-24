import numpy as np


def gaussElimination(matrixA, matrixB):
    if matrixA.shape[0] != matrixA.shape[1]:
        print("Error: Square matrix is not given")
        return

    if matrixB.shape[1] > 1 or matrixB.shape[0] != matrixA.shape[0]:
        print("Error: Constant vector incorrectly size")
        return

    n = len(matrixB)
    m = n - 1
    i = 0
    j = i - 1
    x = np.zeros(n)

    augmentedMatrix = np.concatenate((matrixA, matrixB), axis=1, dtype=float)
    print("The initial augmented matrix is: \n {augmentedMatrix}")
    print("Solving for the upper-triangular matrix:")

    while i < n:
        if augmentedMatrix[i][i] == 0.0:
            print("Error: Division by zero")
            return

        for j in range(i + 1, n):
            scalingFactor = augmentedMatrix[j][i] / augmentedMatrix[i][i]
            augmentedMatrix[j] = augmentedMatrix[j] - \
                (scalingFactor * augmentedMatrix[i])
            print(augmentedMatrix)

        i += 1

    x[m] = augmentedMatrix[m][n] / augmentedMatrix[m][m]

    for k in range(n-2, -1, -1):
        x[k] = augmentedMatrix[k][n]

        for j in range(k + 1, n):
            x[k] = x[k] - augmentedMatrix[k][j] * x[j]
            x[k] = x[k] / augmentedMatrix[k][k]

    print("The following x-vector matrix solves the above augmented matrix:")
    for answer in range(n):
        print(f"x{answer} is {x[answer]}")


variableMatrix = np.array([[1, 1, 3], [0, 1, 3], [-1, 3, 0]])
constantMatrix = np.array([[1], [3], [5]])

gaussElimination(variableMatrix, constantMatrix)
