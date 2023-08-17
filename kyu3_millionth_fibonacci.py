import numpy as np


def fib(n):
    if n == 0:
        return 0
    if n < 0:
        return np.power(-1, -n + 1) * fib(-n)
    # dtype=object to use python native integers which have unlimited size
    basic_matrix = np.array([[0, 1], [1, 1]], dtype=object)
    initial_array = np.array([[0], [1]], dtype=object)
    matrix = np.linalg.matrix_power(basic_matrix, n - 1)
    [[_], [fn]] = np.matmul(matrix, initial_array)
    return fn
