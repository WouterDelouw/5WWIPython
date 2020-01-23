#INVOER
getal = str(input('geef een getal: '))
letter = ''
deler = 0
#BEREKENINGEN
for letter in getal:
    deler += int(letter)
    letter = ''
if int(getal) % deler == 0:
    uitvoer = ''
else:
    uitvoer = 'g'
#UITVOER
print(getal + ' is ' + uitvoer + 'een Harshadgetal')

