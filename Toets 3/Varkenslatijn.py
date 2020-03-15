def verwijder_medeklinkers(woord):
    varkenslatijnswoord = ''
    stop = 0
    for letter in woord:
        if stop == 0:
            if letter != 'a' and letter != 'e' and letter != 'i' and letter != 'o' and letter != 'u':
                varkenslatijnswoord = varkenslatijnswoord
            else:
                varkenslatijnswoord += letter
                stop = 1
        else:
            varkenslatijnswoord += letter
    return varkenslatijnswoord

def varkenslatijn(tekst):
    eind = 0
    uitgang = ''

    for letter in tekst:
        if eind != 0:
            if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
                uitgang = 'ibus'
            eind = 1


        if uitgang != 'ibus':
            teller = 0
            for letter in tekst:
                teller += 1
                if teller == len(tekst) - 1:
                    if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
                        uitgang = 'nt'
                    else:
                        uitgang = ''

        if uitgang != 'ibus' and uitgang != 'nt':
            tekst = verwijder_medeklinkers(tekst)
    tekst = tekst + uitgang



    nieuw = ''
    for letter in tekst:
        if letter == 'j':
            nieuw += 'i'
        elif letter == 'y' or letter == 'z':
            nieuw = nieuw
        else:
            nieuw += letter

    return nieuw














