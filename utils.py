import typing
import random


def multiply_matrix(
    matrix_a: typing.List[typing.List[int]], matrix_b: typing.List[typing.List[int]]
) -> typing.List[typing.List[int]]:
    c = [[] for _ in range(len(matrix_a))]
    for i in range(len(matrix_a)):
        for j in range(len(matrix_a)):
            sum = 0
            for k in range(len(matrix_a)):
                sum += matrix_a[i][k] * matrix_b[k][j]
            c[i].append(sum)

    return c


def create_non_singular_matrix(size: int) -> typing.List[typing.List[int]]:
    matrix = [[0] * size for _ in range(size)]

    for i in range(size):
        for j in range(size):
            matrix[i][j] = (i + 1) * (j + 1) + random.randint(-5, 5)

    matrix[size - 1], matrix[size - 2] = matrix[size - 2], matrix[size - 1]

    return matrix


def calculate_determinant(matrix: typing.List[typing.List[int]]) -> float:
    """
    Calculate the determinant of a square matrix iteratively.
    """
    n = len(matrix)

    if n != len(matrix[0]):
        raise ValueError("The matrix must be square.")

    det = 0

    temp = [row[:] for row in matrix]

    for k in range(n - 1):
        for i in range(k + 1, n):
            factor = temp[i][k] / temp[k][k]
            for j in range(k, n):
                temp[i][j] -= factor * temp[k][j] # type: ignore

    det = 1
    for i in range(n):
        det *= temp[i][i]

    return det
