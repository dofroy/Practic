def duplicate_count(text):
    text = text.lower()
    lst = [i for i in set(text) if text.count(i) >= 2]
    return len(lst)
