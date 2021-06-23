import csv

glossary = {}

with open('PoliMorf.tab', 'r', encoding='utf-8') as miniMorf:
    csvreader = csv.reader(miniMorf, delimiter='\t')
    for row in csvreader:
        # wrzucam tylko niepowtarzające się słowa, zakładając, że w słowniku w pierwszej kolejności pojawia się słowo
        # w najbardziej "podstawowej formie", skoro interesuje mnie jedynie jaka jest to część mowy
        if row[0] not in glossary.keys():
            glossary[row[0]] = (row[1], row[2])


interpretation_dic = {'subst': 'rzeczownik',
                      'depr': 'rzeczownik, forma depracjatywna',
                      'num': 'liczebnik główny',
                      'numcol': 'liczebnik zbiorowy',
                      'adj': 'przymiotnik',
                      'adja': 'przymiotnik przyprzymiotnikowy',
                      'adjp': 'przymiotnik poprzyimkowy',
                      'adjc': 'przymiotnik predakatywny',
                      'adv': 'przysłówek',
                      'ppron12': 'zaimek nietrzecioosobowy',
                      'ppron13': 'zaimek trzecioosobowy',
                      'siebie': 'zaimek SIEBIE',
                      'fin': "forma przeszła czasownika",
                      'bedzie': 'forma przyszła czasownika BYĆ',
                      'aglt': 'aglutynant czasownika BYĆ',
                      'praet': 'pseudoimiesłów',
                      'impt': 'rozkaźnik',
                      'imps': 'bezosobnik',
                      'inf': 'bezokolicznik',
                      'pcon': 'imiesłów przysłówkowy współczesny',
                      'pant': 'imiesłów przysłówkowy uprzedni',
                      'ger': 'odsłownik',
                      'pact': 'imiesłów przymiotnikowy czynny',
                      'ppas': 'imiesłów przymiotnikowy bierny',
                      'winien': 'czasownik typu WINIEN (forma teraźniejsza)',
                      'pred': 'predykatyw',
                      'prep': 'przyimek',
                      'conj': 'spójnik współrzędny',
                      'comp': 'spójnik podrzędny',
                      'interj': 'wykrzyknik',
                      'burk': 'burkinostka',
                      'qub': 'kublik',
                      'brev': 'skrót',
                      'xxx': 'ciało obce',
                      'interp': 'interpunkcja'}


def interpretation(tagset, int_dic):
    temp = tagset.find(':')
    simple = tagset[:temp]
    return int_dic[simple]


word = input('Podaj słowo: ')

lemmaOfInput = glossary[word]
lemmaOfInput = lemmaOfInput[0]

tagsetOfLemma = glossary[lemmaOfInput]
tagsetOfLemma = tagsetOfLemma[1]
typeOfLemma = interpretation(tagsetOfLemma, interpretation_dic)

print('Forma podstawowa:  ' + lemmaOfInput + '  -  ' + typeOfLemma)
