def isLeapYear(year):
    if year % 4 == 0 and (year % 400 == 0 or not year % 100 == 0):
        return True
    return False
