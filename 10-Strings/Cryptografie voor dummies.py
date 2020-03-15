def versleutel_woord(woord, verschuiving):
    nieuw = ''
    for letter in woord:
        if 97 <= ord(letter) <= 127:
            letter = letter.upper()
        if ord(letter) + verschuiving <= 127:
            letter = chr(ord(letter) + verschuiving)
        else:
            letter = chr(ord(letter) + verschuiving - 127 + 32)
        if letter == '@':
            letter = ' '
        nieuw += letter
    return nieuw



def versleutel_zin(zin, verschuiving):
    nieuwe_zin = ''
    zin = zin.split(' ')
    for woord in zin:
        nieuwe_zin += versleutel_woord(woord, verschuiving)
        if zin.index(woord) + 1 != len(zin):
            nieuwe_zin += '@'
    return nieuwe_zin

