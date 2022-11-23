def filter_list(lst):
    lst = [i for i in lst if i != str(i)]
    return lst
print(filter_list([1, 2, 3, 'a', 123, 'c']))