"""
https://www.codewars.com/kata/52b7ed099cdc285c300001cd/train/python
"""


def sum_of_intervals(intervals):
    a = sorted([list(i) for i in intervals])
    l = [a[0]]
    for i in a:
        if l[-1][0] <= i[0] <= l[-1][1] and l[-1][0] <= i[1] <= l[-1][1]:  # 1 in 2 in
            continue
        elif l[-1][0] <= i[0] <= l[-1][1] <= i[1]:  # 1 in 2 out
            l[-1][1] = i[1]
        elif l[-1][0] <= i[0] >= l[-1][1]:  # 1 out 2 out
            l.append(i)

    return sum(map(lambda x: x[1] - x[0], l))
