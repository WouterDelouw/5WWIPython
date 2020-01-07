# invoer
n = (int(input('Hoeveelste getal in rij? '))) - 2
# berekeningen
getal_1, getal_2, getal_n = 1, 1, 1
for i in range(n):
    getal_n = (getal_1 + getal_2)
    getal_1 = getal_2
    getal_2 = getal_n
#uitvoer
print(getal_n)
