# invoer
t = int(input('geef aantal seconden: '))
stappen_vooruit = 0
stappen_achteruit = 0
aantal_stappen = 0
# berekeningen
for i in range(1, t+1):
    if t % 2 != 0:
        aantal_stappen += 2*i
    else:
        aantal_stappen -= i

aantal_stappen = stappen_vooruit - stappen_achteruit

# uitvoer
print(aantal_stappen)
