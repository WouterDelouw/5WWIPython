
def is_letter(karakter):
    if ord('a') <= ord(str(karakter)) <= ord('z') or ord('A') <= ord(str(karakter)) <= ord('Z'):
        return True
    else:
        return False




def roteer_letter(letter, verschuiving):
    if ord('a') <= ord(letter) <= ord('z'):
        if ord(letter) + verschuiving > ord('z'):
            letter_nieuw = chr(ord('a') + (verschuiving - (ord('z') - ord(letter) + 1)))
        else:
            letter_nieuw = chr(ord(letter) + verschuiving)
        return letter_nieuw
    elif ord('A') <= ord(letter) <= ord('Z'):
        if ord(letter) + verschuiving > ord('Z'):
            letter_nieuw = chr(ord('A') + (verschuiving - (ord('Z') - ord(letter) + 1)))
        else:
            letter_nieuw = chr(ord(letter) + verschuiving)
        return letter_nieuw




def versleutel(tekst, caesarcijfer):
    nieuwe_tekst = ''
    for letter_a in tekst:
        if ord('a') <= ord(letter_a) <= ord('z') or ord('A') <= ord(letter_a) <= ord('Z'):
            nieuwe_tekst += roteer_letter(letter_a, caesarcijfer)
        else:
            nieuwe_tekst += letter_a
    return nieuwe_tekst

