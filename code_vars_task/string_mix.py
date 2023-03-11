import re, string
w = string.ascii_lowercase[::-1]

def del_uppercase(s):
    return re.sub(r'[A-Z\W\d ]', '', s)


def str_to_dict(s):
    d = {}
    for i in s:
        d[i] = d.get(i, 0) + 1
    return d


def del_1(d):
    return {i: j for i, j in d.items() if j > 1}


def dict_to_list(d):
    return [i * j for i, j in d.items()]


s1="Are the kids at home? aaaaa fffff"
s2="Yes they are here! aaaaa fffff"

s1 = dict_to_list(del_1(str_to_dict(del_uppercase(s1))))
s2 = dict_to_list(del_1(str_to_dict(del_uppercase(s2))))

k = ''
n = 0
while len(s1 + s2) != 0:
    try:
        x = max(s1, key=lambda i: len(i))
    except ValueError:
        x = ('0')
    try:
        y = max(s2, key=lambda j: len(j))
    except ValueError:
        y = ('0')
    if x[0] == y[0]:
        if x == y:
            k += '=:' + x
            s1.remove(x)
            s2.remove(y)
        elif x > y:
            k += '1:' + x
            s1.remove(x)
            s2.remove(y)
        elif x < y:
            k += '2:' + y
            s1.remove(x)
            s2.remove(y)
    else:
        if len(x) == len(y):
            c = max(x, y, key=lambda i: w.find(i[0]))
            if c == x:
                k += '1:' + x
                s1.remove(x)
                l1 = [i[0] for i in s2]
                if x[0] in l1:
                    del s2[l1.index(x[0])]
            else:
                k += '2:' + y
                s2.remove(y)
                l2 = [i[0] for i in s1]
                if y[0] in l2:
                    del s1[l2.index(y[0])]
        elif len(x) > len(y):
            k += '1:' + x
            s1.remove(x)
            l1 = [i[0] for i in s2]
            if x[0] in l1:
                del s2[l1.index(x[0])]
        elif len(x) < len(y):
            k += '2:' + y
            s2.remove(y)
            l2 = [i[0] for i in s1]
            if y[0] in l2:
                del s1[l2.index(y[0])]

print(k)
