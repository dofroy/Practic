def is_pangram(s):
    lst = [i for i in set(s.lower()) if i.isalpha()]
    return len(lst) == 26
