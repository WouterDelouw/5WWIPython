# invoer
kleur_1 = str(input('kleur 1: '))
kleur_2 = str(input('kleur 2: '))
omgekeerde_kleur = int(input('persoon 1 of 2 die omgekeerde kleur zegt?: '))

# berekeningen
if omgekeerde_kleur == 1:
    uitspraak_2 = kleur_1
    if kleur_2 == 'zwart':
        uitspraak_1 = 'wit'
    else:
        uitspraak_1 = 'zwart'
else:
    uitspraak_1 = kleur_2
    if kleur_1 == 'zwart':
        uitspraak_2 = 'wit'
    else:
        uitspraak_2 = 'zwart'



# uitvoer

print(uitspraak_1)
print(uitspraak_2)

