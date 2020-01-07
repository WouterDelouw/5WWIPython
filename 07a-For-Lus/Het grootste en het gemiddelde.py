# invoer
aantal_getallen = int(input('aantal getallen: '))

getal_0 = int(input('geef getal : ' ))

som, grootste = getal_0, getal_0



for i in range(aantal_getallen - 1):
    getal = int(input('geef getal : '))
    som += getal
    grootste = max(grootste, getal)

gemiddelde = som / aantal_getallen

uitvoer = 'Het grootste getal is {:.0f} en het gemiddelde is {:.2f}'
print(uitvoer.format(grootste, gemiddelde))
