# invoer
snelheid = int(input('windsnelheid: '))

# berekeningen
if snelheid < 119:
    uitvoer = 'geen orkaan'
else:
    if 119 <= snelheid <= 153:
        uitvoer = 'categorie 1'
    else:
         if 154 <= snelheid <= 177:
            uitvoer = 'categorie 2'
         else:
             if 178 <= snelheid <= 209:
                uitvoer = 'categorie 3'
             else:
                 if 210 <= snelheid <= 249:
                    uitvoer = 'categorie 4'
                 else:
                     uitvoer = 'categorie 5'

# uitvoer
print(uitvoer)
