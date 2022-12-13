def generate_ip():
    import random
    lst = [str(random.randrange(0, 256)) for _ in range(4)]
    return ".".join(lst)
