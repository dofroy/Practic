def ordered_count(inp):
    mset = inp.replace(" ", "")
    lst = [(i, inp.count(i)) for i in mset]  
    return lst
print(ordered_count('abracadabra'))