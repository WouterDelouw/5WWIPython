# invoer
dikte = int(input('geef de dikte van het papier in mm: '))
afstand = int(input('geef de afstand: '))
aantal_vouwen = 0
# berekeningen
while dikte < afstand:
    dikte = (dikte * 2)
    aantal_vouwen += 1
# uitvoer
print('Na', aantal_vouwen, 'keer vouwen bedraagt de dikte van het papier', dikte, 'mm.')
