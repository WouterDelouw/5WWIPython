# invoer
getal = float(input('geef een getal tussen 0 en 1: '))
som, exponent = 0, 0
# berekeningen
while som < getal:
    exponent += 1
    som += (1 / (pow(2, exponent)))
# uitvoer
print(exponent, som)
