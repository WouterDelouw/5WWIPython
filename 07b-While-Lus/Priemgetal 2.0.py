getal = int(input('geef een getal: '))
deelbaar = 0
ondeelbaar = 0
deler = 2
while deelbaar == 0 or ondeelbaar > getal:
    if getal % deler == 0:
        deelbaar += 1
    else:
        ondeelbaar += 1

if deelbaar != 0:
    uitvoer = 'is geen priemgetal'
else:
    uitvoer = 'is een priemgetal'

print(getal, uitvoer)
