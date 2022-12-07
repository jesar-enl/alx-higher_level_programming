#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    mat = []
    for i in matrix:
        a = list(map(lambda x: x * x, i))
        mat.append(a)
    return mat
