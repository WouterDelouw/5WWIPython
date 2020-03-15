import math
pi = math.pi


# invoer
getal = (input('geef een getal: '))
coordinaat = [0, 0]

# berekeningen
for cijfer in getal:
    if cijfer != '.':
        coordinaat[0] += (math.sin(int(cijfer) * 36 * (pi / 180)))
        coordinaat[1] += (math.cos(int(cijfer) * 36 * (pi / 180)))

#uitvoer
uitvoer = 'Number ' + getal + ' walks to position ({:.2f}, {:.2f}).'
print(uitvoer.format(coordinaat[0], coordinaat[1]))
