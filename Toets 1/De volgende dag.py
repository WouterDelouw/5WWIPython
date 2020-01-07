# invoer
dag = int(input('geef de dag: '))
maand = int(input('geef de maaand '))
jaar = int(input('geef het jaar: '))

# berekeningen
if dag == 31:
    if maand != 12:
        nieuwe_dag = 1
        nieuwe_maand = maand + 1
        nieuw_jaar = jaar
    else:
        nieuwe_dag = 1
        nieuwe_maand = maand + 1
        nieuw_jaar = jaar + 1
elif dag == 30:
    if maand == 4 or maand == 6 or maand == 9 or maand == 11:
        nieuwe_dag = 1
        nieuwe_maand = maand + 1
        nieuw_jaar = jaar
    else:
        nieuwe_dag = dag + 1
        nieuwe_maand = maand
        nieuw_jaar = jaar
elif dag == 29 and maand == 2:
    nieuwe_maand = 3
    nieuwe_dag = 1
    nieuw_jaar = jaar
elif dag == 28 and maand == 2:
    if jaar % 4 == 0 and jaar % 400 == 0:
        nieuwe_dag = 29
        nieuwe_maand = 2
        nieuw_jaar = jaar
    elif jaar % 4 == 0 and jaar % 100 == 0:
        nieuwe_maand = 3
        nieuwe_dag = 1
        nieuw_jaar = jaar
    elif jaar % 4 == 0:
        nieuwe_dag = 29
        nieuwe_maand = 2
        nieuw_jaar = jaar
    else:
        nieuwe_maand = 3
        nieuwe_dag = 1
        nieuw_jaar = jaar
else:
    nieuwe_dag = dag + 1
    nieuwe_maand = maand
    nieuw_jaar = jaar

# uitvoer
print(str(nieuwe_dag) + '/' + str(nieuwe_maand) + '/' + str(nieuw_jaar))
