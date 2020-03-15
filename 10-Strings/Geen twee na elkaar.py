def ontdubbelen(woord):
    vorige_letter, nieuw_woord = ' ', ''
    for letter in woord:
        if vorige_letter != letter:
            nieuw_woord += letter
        vorige_letter = letter
    return nieuw_woord
