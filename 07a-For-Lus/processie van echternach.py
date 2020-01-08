# invoes
seconden = (int(input('geef aantal seconden: ')) + 1)
aantal_stappen = 0
# berekeningen
for i in range(seconden):
    if (i % 2) != 0:
        aantal_stappen += (i + 1)
    else:
        aantal_stappen -= (i / 2)

# uitvoer
print(int(aantal_stappen))
