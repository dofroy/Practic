def array_diff(a, b):
    mset = set(a).difference(set(b))
    return sorted(mset)

print(array_diff([1,2,2], [1]))