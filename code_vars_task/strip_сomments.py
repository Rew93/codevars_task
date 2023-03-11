'''
https://www.codewars.com/kata/51c8e37cee245da6b40000bd/train/python
'''


def strip_comments(a, markers):
    lst = a.split('\n')
    for i in range(len(lst)):
        for j in markers:
            k = lst[i].rfind(j)
            if k != -1:
                lst[i] = lst[i][:k].rstrip()

    return '\n'.join(lst)
