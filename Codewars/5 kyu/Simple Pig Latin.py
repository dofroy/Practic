def pig_it(text):
    text1 = [i[1::] + i[0] + "ay" if i not in "!?.,-+:;" else i for i in text.split()]
    return " ".join(text1)


