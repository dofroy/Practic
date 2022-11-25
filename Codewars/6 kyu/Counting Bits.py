def count_bits(n):
    num = str(bin(int(n))[2:])
    return len([i for i in num if i == '1'])
