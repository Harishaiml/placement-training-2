def rotate(matrix):
    matrix[:] = list(zip(*matrix[::-1]))
