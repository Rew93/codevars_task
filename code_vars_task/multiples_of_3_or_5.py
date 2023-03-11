import pytest

"""
https://www.codewars.com/kata/514b92a657cdc65150000006/train/python
"""


def solution(number):
    total = 0
    if number > 3:
        for i in range(2, number):
            if i % 3 == 0 or i % 5 == 0:
                total += i
    return total