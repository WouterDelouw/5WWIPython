def printbaar_rek(configuratie):
    print = ''
    for i in range(len(configuratie)):
        for j in range(len(configuratie[i])):
            print += configuratie[-(i + 1)][j]
        if i + 1 != len(configuratie):
            print += '\n'
    return print


def speel(kleur, kolom, rekken):
    teller = 0
    stop = False
    while stop == False:
        if rekken[teller][kolom] == 'O':
            rekken[teller][kolom] = kleur
            stop = True
        else:
            teller += 1
    return rekken
