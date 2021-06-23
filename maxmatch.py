def MaxMatch(line, dictionary):
    if not line:
        return ""

    for a in range(len(line), 0, -1):
        first = line[:a]
        rest = line[a:]
        if first in dictionary:
            return first + ' ' + MaxMatch(rest, dictionary)

    # failed to find a word
    first = line[0]
    rest = line[1:]
    return first + ' ' + MaxMatch(rest, dictionary)


def Dictionary(file_name):
    dictionary = {}

    with open(file_name, 'r', encoding='utf-8') as morpheus:
        for line in morpheus:
            dictionary[line.strip()] = 1
    return dictionary


sentence = input('Podaj zdanie: \n')
dictionary = Dictionary('PoliMorfShort.tab')
print('\nWynik: \n' + MaxMatch(sentence, dictionary))













