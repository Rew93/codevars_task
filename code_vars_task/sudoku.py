"""
https://www.codewars.com/kata/5296bc77afba8baa690002d7/train/python
"""


def sudoku(puzzle):
    """return the solved puzzle as a 2d array of 9 x 9"""

    l = [(0, 3, 0, 3), (0, 3, 3, 6), (0, 3, 6, 9), (3, 6, 0, 3), (3, 6, 3, 6), (3, 6, 6, 9), (6, 9, 0, 3), (6, 9, 3, 6),
         (6, 9, 6, 9)]

    while True:
        count = len([0 for i in range(9) for j in range(9) if puzzle[i][j] == 0])
        if count == 0:
            break
        for i in range(9):
            for j in range(9):
                if puzzle[i][j] == 0:
                    check_x = puzzle[i]
                    check_y = [n[j] for n in puzzle]
                    check_z = []
                    for h in range(len(l)):
                        if l[h][0] <= i < l[h][1] and l[h][2] <= j < l[h][3]:
                            for a in range(l[h][0], l[h][1]):
                                for b in range(l[h][2], l[h][3]):
                                    check_z.append(puzzle[a][b])
                    ver = list(i for i in range(1, 10) if i not in check_x and i not in check_y and i not in check_z)
                    if len(ver) == 1:
                        puzzle[i][j] = ver[0]
                    else:
                        puzzle[i][j] = 0
                check_x = 0
                check_y = 0
                check_z = 0

    return puzzle
