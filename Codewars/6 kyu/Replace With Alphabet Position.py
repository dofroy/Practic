def alphabet_position(text):
    alph = 'abcdefghijklmnopqrstuvwxyz'
    lst1 = [str(alph.find(i) + 1) for i in text.lower() if i in alph]
    return " ".join(lst1)
