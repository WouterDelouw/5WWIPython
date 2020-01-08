# invoer
snelheid_stijn = int(input('geef de snelheid van stijn in meter per seconde: '))
snelheid_kaat = int(input('geef de snelheid van kaat in meter per seconde: '))
afstand = int(input('geef de afstand tussen de huizen in meter: '))
seconden = 0

# berekeningen
while afstand > 0:
    afstand -= (snelheid_kaat + snelheid_stijn)
    seconden += 1

# uitvoer
print('Na', seconden, 's hebben Stijn en Kaat elkaar ontmoet.')
