'''
https://www.codewars.com/kata/521c2db8ddc89b9b7a0000c1/train/python
'''


def snail(snail_map):
    lst = []
    n = 0
    while True:
        try:
            lst.extend([x for x in snail_map[0 + n][0 + n:len(snail_map[0]) - n]])
            lst.extend([x[len(snail_map) - 1 - n] for x in snail_map[1 + n: len(snail_map) - n]])
            lst.extend([x for x in snail_map[len(snail_map) - 1 - n][::-1][1 + n:len(snail_map) - n]])
            lst.extend([x[0 + n] for x in snail_map[len(snail_map) - 2 - n:0 + n:-1]])
        except IndexError:
            break
        n += 1
    return lst
