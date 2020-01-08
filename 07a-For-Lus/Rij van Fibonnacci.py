getal_1, getal_2, getal_n = 1, 1, 1
for i in range((int(input('Hoeveelste getal in rij? '))) - 2):
    getal_n = (getal_1 + getal_2)
    getal_1 = getal_2
    getal_2 = getal_n
print(getal_n)
