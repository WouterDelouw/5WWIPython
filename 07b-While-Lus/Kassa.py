som = 0
nul = 0
while nul == 0:
    prijs = float(input('prijs: '))
    if prijs == 0:
        nul += 1
    else:
        som += prijs
uitvoer = 'De totale prijs is € {:.2f}'
print(uitvoer.format(som))
