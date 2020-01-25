def germaniseer(zin):
    nieuwe_zin = ''
    hoofdletter = 1
    for letter in zin:
        if hoofdletter == 1:
            nieuwe_zin += letter.upper()
        else:
            nieuwe_zin += letter
        if letter == ' ':
            hoofdletter = 1
        else:
            hoofdletter = 0
    return nieuwe_zin
