# invoer
getal_a = int(input('geef het getal a: '))
getal_b = int(input('geef het getal b: '))
som_a, som_b = 0, 0
# berekeningen
#  som a berekenen
for i in range(1, getal_a):
    if getal_a % i == 0:
        som_a += i
#  som b berekenen
for k in range(1, getal_b):
    if getal_b % k == 0:
        som_b += k
#  checken of ze bevriend zijn
if getal_a == som_b and getal_b == som_a:
    uitvoer = '{:.0f} en {:.0f} zijn bevriende getallen'
else:
     uitvoer = '{:.0f} en {:.0f} zijn geen bevriende getallen'
# uitvoer
print(uitvoer.format(getal_a, getal_b))


