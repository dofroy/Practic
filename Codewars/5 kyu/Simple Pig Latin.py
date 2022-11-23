def pig_it(text):
    text1 = []
    for i in text.split():
        if i not in "!,.::?" :
            text1.append(i[1:] + i[0] + "ay")
        else:
            text1.append(i)

    return " ".join(text1)


print(pig_it('Hello world !'))
