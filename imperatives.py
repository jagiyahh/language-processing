import nltk

#tryb rozkazujący dla zdań prostych

def verifyImperative(sen):
    tokens = nltk.word_tokenize(sen)
    tags = nltk.pos_tag(tokens)
    print(tags)
    
    #wnioskuję czy to pytane po interpunkcji
    if '?' in tokens:
        return('END')
    
    #pozbywam się znaków interpunkcyjnych ( pomijając ?)
    if tokens[-1] in ('.', '!'):
        del tokens[-1]
        del tags[-1]
    
    for x in range(len(tags)):
        #sprawdzam rzeczowniki lub zaimki na początku zdania
        if tags[x][1] in ('PRP', 'NN', 'NNS', 'NNP', 'NNPS'):
            return('END')

        #szukam czasownika przed rzeczownikiem/przecinkiem zgodnie z regułami zdań rozkazującyh w j angielskim
        if tags[x][1] in ('VB'):
            print('Zdanie zawiera rozkaz.')
            return('Akcja: ' + tags[x][0] + '. Obiekt: ' +' '.join(tokens[x+1:]) + '.')
    return('END')
    
    
zdanie = input('Podaj zdanie:\n>> ')
print(verifyImperative(zdanie))
