import re, operator

d = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
}

redex_brackets = re.compile(r'\(.*\)')
redex = re.compile(r"(?<=\().*?((-)?\d+\.?\d*)([/*])(-?\d+\.?\d*).*(?=\))")
redex_1 = re.compile(r"(?<=\().*?((-)?\d+\.?\d*)([+-])(\d+\.?\d*).*(?=\))")
redex_2 = re.compile(r'(\(+)(-?\d+\.?\d*)(\)+)')
redex_3 = re.compile(r"((^-)?\d+\.?\d*)([/*])(-?\d+\.?\d*)")
redex_4 = re.compile(r"((^-)?\d+\.?\d*)([+-])(\d+\.?\d*)")
redex_5 = re.compile(r'(?<=[+-/*(]) ?- (?=\(|\d)')


def del_gap(example):
    return example.replace(' ', '')


def func(example, regular):
    while regular.search(example) is not None:
        s = regular.search(example)
        s1 = s.group(1)
        s2 = s.group(3)
        s3 = s.group(4)
        s4 = d[s2](float(s1.strip()), float(s3.strip()))
        example = example.replace(s1 + s2 + s3, str(s4)).replace('--', '+')
    return example


def func_del_brackets(example, regular):
    while regular.search(example) is not None:
        sss = regular.search(example)
        s1 = sss.group(1)
        s2 = sss.group(2)
        s3 = sss.group(3)
        if len(s1) == len(s3):
            s4 = s2
        elif len(s1) > len(s3):
            s4 = ((len(s1) - len(s3)) * '(') + s2
        else:
            s4 = s2 + ((len(s3) - len(s1)) * ')')

        if example[sss.group(0).span()[0]-2] not in ['/', '*', '+', '-']:
            example = example.replace(sss.group(0), s4).replace('--', '+')
        else:
            example = example.replace(sss.group(0), s4).replace('--', '')
    return example


def calc(s):
    if redex_5.search(s) is None:
        s = del_gap(s)
        s = re.sub(r'--', '+', s)
        s = re.sub(r'\+-', '-', s)
        while redex_brackets.search(s) is not None:
            s = func_del_brackets(s, redex_2)
            s = func(s, redex)
            s = func(s, redex_1)
        while True:
            try:
                float(s)
                break
            except ValueError:
                s = func(s, redex_3)
                s = func(s, redex_4)
        return int(s[:len(s) - 2]) if s[len(s) - 2:] == '.0' else float(s)
    else:
        return 'Invalid'


