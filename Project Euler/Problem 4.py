def problem_4():
    lst = []
    for i in range(100, 1000):
        total = 0
        for j in range(100, 1000):
            total = i * j
            if str(total) == str(total)[::-1]:
                lst.append(total)
    return max(lst)


print(problem_4())
