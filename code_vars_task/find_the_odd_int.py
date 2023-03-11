def find_it(seq):
    new_seq = set(seq)
    for i in new_seq:
        q = seq.count(i)
        if q % 2 != 0:
            return i

