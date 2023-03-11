"""
https://www.codewars.com/kata/5266876b8f4bf2da9b000362/train/python
"""


# []                                -->  "no one likes this"
# ["Peter"]                         -->  "Peter likes this"
# ["Jacob", "Alex"]                 -->  "Jacob and Alex like this"
# ["Max", "John", "Mark"]           -->  "Max, John and Mark like this"
# ["Alex", "Jacob", "Mark", "Max"]  -->  "Alex, Jacob and 2 others like this"

def likes(names):
    if len(names) == 0:
        s = 'no one likes this'
    elif len(names) == 1:
        s = f'{names[0]} likes this'
    elif len(names) == 2:
        s = f'{names[0]} and {names[1]} like this'
    elif len(names) == 3:
        s = f'{names[0]}, {names[1]} and {names[2]} like this'
    else:
        s = ', '.join(names[:2]) + f' and {len(names) - 2} others like this'
    return s
