'''
https://www.codewars.com/kata/5263c6999e0f40dee200059d/train/python
'''


def comb_for_2key(num):
    lst = []
    for i in num[0]:
        for j in num[1]:
            lst.append(i + j)
    return sorted(lst)


def comb_for_3key(num):
    lst = []
    for i in num[0]:
        for j in num[1]:
            for k in num[2]:
                lst.append(i + j + k)
    return sorted(lst)


def comb_for_4key(num):
    lst = []
    for i in num[0]:
        for j in num[1]:
            for k in num[2]:
                for n in num[3]:
                    lst.append(i + j + k + n)
    return sorted(lst)


def comb_for_5key(num):
    lst = []
    for a in num[0]:
        for b in num[1]:
            for c in num[2]:
                for d in num[3]:
                    for i in num[4]:
                        lst.append(a + b + c + d + i)
    return sorted(lst)


def comb_for_6key(num):
    lst = []
    for a in num[0]:
        for b in num[1]:
            for c in num[2]:
                for d in num[3]:
                    for i in num[4]:
                        for f in num[5]:
                            lst.append(a + b + c + d + i + f)
    return sorted(lst)


def comb_for_7key(num):
    lst = []
    for a in num[0]:
        for b in num[1]:
            for c in num[2]:
                for d in num[3]:
                    for i in num[4]:
                        for f in num[5]:
                            for g in num[6]:
                                lst.append(a + b + c + d + i + f + g)
    return sorted(lst)


def comb_for_8key(num):
    lst = []
    for a in num[0]:
        for b in num[1]:
            for c in num[2]:
                for d in num[3]:
                    for i in num[4]:
                        for f in num[5]:
                            for g in num[6]:
                                for h in num[7]:
                                    lst.append(a + b + c + d + i + f + g + h)
    return sorted(lst)


def get_pins(obs):

    dic = {'1': ['1', '2', '4'],
           '2': ['1', '2', '3', '5'],
           '3': ['2', '3', '6'],
           '4': ['1', '4', '5', '7'],
           '5': ['2', '4', '5', '6', '8'],
           '6': ['3', '5', '6', '9'],
           '7': ['4', '7', '8'],
           '8': ['5', '7', '8', '9', '0'],
           '9': ['8', '9', '6'],
           '0': ['8', '0']}
    num = [dic[i] for i in obs]
    if len(obs) == 1:
        return dic[obs]
    elif len(obs) == 2:
        return comb_for_2key(num)
    elif len(obs) == 3:
        return comb_for_3key(num)
    elif len(obs) == 4:
        return comb_for_4key(num)
    elif len(obs) == 5:
        return comb_for_5key(num)
    elif len(obs) == 6:
        return comb_for_6key(num)
    elif len(obs) == 7:
        return comb_for_7key(num)
    else:
        return comb_for_8key(num)
