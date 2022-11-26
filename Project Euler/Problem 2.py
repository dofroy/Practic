def problem_2():
    a, b = 1, 1
    count = 0
    while b < 4_000_000:
        a, b = b, a + b
        if b % 2 == 0:
            count += b
    return count


print(problem_2())