"""

"""
def spiralize(size):
    matrix = [[1] * size for i in range(size)]
    n = 0
    k = size // 2 if size // 2 % 2 == 0 else size // 2 + 1
    while n != k:
        for i in range(size):
            for j in range(size):
                if i == 1 + n and len(matrix) - 1 - n > j >= 0 + n:  # top
                    matrix[i][j] = 0
                if len(matrix) - 1 - n > i > 1 + n and j == len(matrix) - 2 - n:  # right
                    matrix[i][j] = 0
                if i == len(matrix) - 2 - n and len(matrix) - 2 - n >= j >= 1 + n:  # down
                    matrix[i][j] = 0
                if len(matrix) - 1 - n > i > 2 + n and j == 1 + n:  # left
                    matrix[i][j] = 0
        n += 2
    return matrix
