def spin_words(sentence):
    lst = [i[::-1] if len(i) >= 5 else i for i in sentence.split()]
    return " ".join(lst)
