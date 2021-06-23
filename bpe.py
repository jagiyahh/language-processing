import re
from collections import Counter


# podstawowa wersja słownika - litery występujące w zdaniu oraz spacja ozn. przez _

def fun_dict(los):
    vocab = set()
    for i in range(len(los)):
        vocab.add(los[i])
    return vocab


# szukam bigramow, łącząc następujące po sobie w liście znaki

def find_bgrms(vocab, tab):
    bigrams = []
    first_let = tab[0]
    for second_let in tab[1:]:
        bigrams.append(first_let + second_let)
        first_let = second_let

    # tworzę słownik z liczebnością wszystkich bigramów
    abundance = Counter(bigrams)

    # szukam najczęściej występującego bigramu
    best_match = max(abundance, key=abundance.get)

    # sklejam bigram w liscie znakow
    rest, last = best_match[:-1], best_match[-1]
    big = rest + last
    tab = glueh(tab, big)

    # dodaję bigram do finalnego słownika
    vocab.add(best_match)

    return vocab, tab


# iteracje algorytmu bpe dla zadanego slownika podstawowego, ciągu znaków oraz zadanej wielkosci finalnego slownika

def bpe(fun_vocab, sen_list, num):

    while len(fun_vocab) < num:
        fun_vocab, sen_list = find_bgrms(fun_vocab, sen_list)

    return fun_vocab


def glueh(sen_list, big):
    temp = len(sen_list) - 2
    for a in range(temp):
        if sen_list[a] == big[0]:
            if sen_list[a+1] == big[1]:
                sen_list[a:a+2] = [''.join(sen_list[a: a+2])]
    return sen_list


corpus = input("Podaj zdanie: ")
number = int(input("Podaj wielkość słownika: "))


# pozbywam się znaków interpunkcyjnych i zamieniam białe znaki na _
corpus = re.sub(r'[\.\?!-_:;,]', '', corpus)
corpus = re.sub(r'[\s\t\n]', '_', corpus)

cor_list = list(corpus)
vocabulary = bpe(fun_dict(corpus), cor_list, number)

print(vocabulary)
print('Liczba wyrazów w słowniku: ' + str(len(vocabulary)))

