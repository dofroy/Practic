def problem_16():
    count = 0
    for i in str(2**1000):
        count += int(i)
    return count


print(problem_16())
