def find_it(seq):
    seq = [i for i in seq if seq.count(i) % 2 == 1]
    return seq[0]