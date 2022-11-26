def problem_6():
    count1 = sum([i for i in range(1, 101)]) ** 2
    count2 = sum([i**2 for i in range(1, 101)])
    return count1 - count2


print(f'Разность: {problem_6()}')

