speler_1 = str(input('speler 1: '))
speler_2 = str(input('speler 2: '))

# berekeningen
if speler_1 == speler_2:
    uitvoer = 'onbeslist'
elif speler_1 == 'blad' and speler_2 == 'schaar':
    uitvoer = 'speler 2 wint'
elif  speler_1 == 'schaar' and speler_2 == 'steen':
    uitvoer = 'speler 2 wint'
elif  speler_1 == 'steen' and speler_2 == 'blad':
    uitvoer = 'speler 2 wint'
elif speler_2 == 'blad' and speler_1 == 'schaar':
    uitvoer = 'speler 1 wint'
elif  speler_2 == 'schaar' and speler_1 == 'steen':
    uitvoer = 'speler 1 wint'
elif  speler_2 == 'steen' and speler_1 == 'blad':
    uitvoer = 'speler 1 wint'

print(uitvoer)
