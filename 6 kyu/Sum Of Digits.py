def digital_root(n):
    count = 0
    count2 = 0
    for i in str(n):
        count += int(i)
    for j in str(count):
        count2 += int(j)
    return count2

print(digital_root(493193))