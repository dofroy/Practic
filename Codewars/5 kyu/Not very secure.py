def alphanumeric(password):
    count = 0
    if password:
        for i in password:
            if i.isalpha() or i.isdigit():
                count += 1
        return count == len(password)
    return False
    pass