def problem_1():
    return sum([i for i in range(1000) if i % 3 == 0 or i % 5 == 0])


print(problem_1())
