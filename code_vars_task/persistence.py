'''
https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec/train/python
'''


def persistence(n):
    count = 0
    while n // 10 != 0:
        n = [int(i) for i in str(n)]
        total = 1
        for i in n:
            total *= i
        n = total
        count += 1
    return count
