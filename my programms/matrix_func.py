def ls(lenght, width, val=0):
    lst = []
    for _ in range(lenght):
        nlst = []
        for _ in range(width):
            nlst.append(val)
        lst.append(nlst)
    return lst


def matrix(lenght=1, width=None, value=0):
    if width is None:
        return ls(lenght, lenght)
    return ls(lenght, width, value)
