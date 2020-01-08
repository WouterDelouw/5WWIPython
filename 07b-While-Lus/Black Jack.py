som = 0
spel = ''

while spel != 'gedaan':
    volgende_kaart = int(input('geef kaart :'))
    som += volgende_kaart
    if som == 21:
        uitvoer = 'Gewonnen!'
        spel += 'gedaan'
    elif som > 21:
        uitvoer = ('Verbrand' + ' (' + str(som) +')')
        spel += 'gedaan'
    elif volgende_kaart == 0:
        uitvoer = ('Voorzichtig gespeeld' + ' (' + str(som) +')')
        spel += 'gedaan'

print(uitvoer)

