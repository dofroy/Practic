def problem_5():
    a = 2520
    b = False
    r = (5, 7, 11, 13, 16, 17, 18, 19)

    while not b:
        for i in r:
            if a % i == 0:
                b = True
                continue
            else:
                b = False
                break
        a += 40

    return a - 40


print(problem_5())

#Help:
#https://github.com/IgorBels/Education/blob/7eb6e95f157ac41b1be02886262c7d0160d2f110/Project%20Euler/Problem%205.py