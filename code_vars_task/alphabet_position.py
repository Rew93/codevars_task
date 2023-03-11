"""
https://www.codewars.com/kata/546f922b54af40e1e90001da/train/python
"""


def alphabet_position(text):
    s = text.lower()
    l = ''
    for i in range(len(s)):
        if s[i].isalpha():
            l += str(ord(s[i]) - 96) + ' '
    return l.rstrip()
