def geldige_zet(zet):
    uitvoer = True
    teller = 0
    for letter in zet:
        teller += 1
        if teller == 1:
            if len(zet) == 3 and (letter == 'K' or letter == 'D' or letter == 'T' or letter == 'L' or letter == 'P'):
                uitvoer = True
            elif len(zet) == 2 and ord('a') <= ord(letter) <= ord('h'):
                uitvoer = True
            else:
                uitvoer = False
        elif teller == 2:
            if len(zet) == 3 and ord('a') <= ord(letter) <= ord('h') and uitvoer != False:
                uitvoer = True
            elif len(zet) == 2 and ord('1') <= ord(letter) <= ord('8') and uitvoer != False:
                uitvoer = True
            else:
                uitvoer = False
        elif teller == 3:
            if len(zet) == 3 and ord('1') <= ord(letter) <= ord('8') and uitvoer != False:
                uitvoer = True
            else:
                uitvoer = False
    return uitvoer


def geldige_zetten(zetten):
    uitvoer = True
    for zet in zetten:
        if geldige_zet(zet) == True and uitvoer != False:
            uitvoer = True
        else:
            uitvoer = False
    return uitvoer
