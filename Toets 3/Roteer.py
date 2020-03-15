def roteer(woord, aantal_letters):
    geroteerd_woord, aantal_letters = '', (aantal_letters % len(woord))
    for i in range(len(woord)):
        if i + aantal_letters <= (len(woord) - 1):
            nieuw = i + aantal_letters
        else:
            nieuw = i - (len(woord) - aantal_letters)
        geroteerd_woord += woord[nieuw]
    return geroteerd_woord
