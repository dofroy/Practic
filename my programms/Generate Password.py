import random


def generate_password(length):
    nums = ['2', '3', '4', '5', '6', '7', '8', '9']
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm',
               'n', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
               'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N',
               'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    s = []
    s1 = ''
    for _ in range(length):
        s += random.sample(nums, random.randint(0, 7))
        s += random.sample(letters, random.randint(0, 48))
    for i in s:
        s1 += i
    return s1[:length]
    pass


def generate_passwords(count, length):
    for i in range(count):
        print(generate_password(length))
    pass


n, m = int(input()), int(input())
generate_passwords(n, m)
