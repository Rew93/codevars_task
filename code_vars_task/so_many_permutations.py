'''
https://www.codewars.com/kata/5254ca2719453dcc0b00027d/train/python
'''
from itertools import permutations as per


def permutations(s):
    s = list(set(per(s)))
    lst = [''.join(i) for i in s]
    return sorted(lst)
