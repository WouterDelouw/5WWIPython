getal = int(input('geef een getal r: '))
som = 0
for i in range(100 // getal + 1):
    som += getal * i
print(som)
