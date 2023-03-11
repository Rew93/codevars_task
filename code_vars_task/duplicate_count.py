def duplicate_count(text):
    text = text.lower()
    l = []
    for i in text:
        l.append(i)
    new_l = set(l)
    return len(list(filter(lambda x: x > 1, (map(lambda x: l.count(x), new_l)))))