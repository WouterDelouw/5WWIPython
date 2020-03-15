def positie_laagste_ascii(string):
    laagste = string[0]
    for letter in string:
        if ord(letter) <= ord(laagste):
            laagste = letter
    return string.index(laagste)




def sorteer(string):
    woord, nieuw_woord = [], ''
    woord += string
    woord.sort()
    for letter in woord:
        nieuw_woord += letter
    return nieuw_woord




def is_alfabetisch(woord):
    if woord == sorteer(woord):
        return True
    else:
        return False
    



