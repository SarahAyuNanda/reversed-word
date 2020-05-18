def rev(sen):
    s = ''
    for i in sen:
        s = i + s
    word = s.split(' ')
    word.reverse()
    return(' '.join(word))


sen = input('Sentence : ')
print(rev(sen))