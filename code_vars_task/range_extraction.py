'''
https://www.codewars.com/kata/51ba717bb08c1cd60f00002f/train/python
'''

lst = [-10, -9, -8, -6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]


def solution(lst):
    lst = lst + [0]
    l = [[lst[0]]]
    result = ''
    for i in range(1, len(lst) - 1):
        if lst[i] - lst[i - 1] == 1 and lst[i] - lst[i + 1] == -1:
            l[-1].append(lst[i])
        elif lst[i] - lst[i - 1] != 1 and lst[i] - lst[i + 1] == -1 and i != 1:
            l[-1].append(lst[i])
        elif lst[i] - lst[i - 1] != 1 and lst[i] - lst[i + 1] == -1 and i == 1:
            l.append([lst[i]])
        else:
            l[-1].append(lst[i])
            l.append([])

    for i in l[:len(l) - 1]:
        if len(i) >= 3:
            result += f'{i[0]}-{i[-1]},'
        elif len(i) == 2:
            result += f'{i[0]},{i[-1]},'
        else:
            result += f'{i[0]},'
    return result[:len(result)-1]
