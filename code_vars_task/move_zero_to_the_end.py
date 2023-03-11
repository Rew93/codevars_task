'''
https://www.codewars.com/kata/52597aa56021e91c93000cb0/train/python
'''


def move_zeros(lst):
    q_zero = lst.count(0)
    lst = list(filter(lambda x: x != 0, lst))
    return lst + [0] * q_zero