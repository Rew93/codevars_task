'''
https://www.codewars.com/kata/5526fc09a1bbd946250002dc/train/python
'''


def find_outlier(integers):
    c = list(filter(lambda x: x % 2 == 0, integers))
    d = list(filter(lambda x: x % 2 != 0, integers))
    return c[0] if len(c) == 1 else d[0]