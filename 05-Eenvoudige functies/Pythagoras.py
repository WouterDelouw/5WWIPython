#92.06826
#16.1
from math import sqrt

# invoer
a = float(input('lenge zijde a:'))
b = float(input('lenge zijde b:'))

# berekeningen
c =  sqrt(pow(a, 2) + pow(b, 2))

# uivoer
uitvoer = 'In een rechthoekige driehoek met rechthoekszijden a = {:.2f} en b = {:.2f} is de schuine zijde {:.2f}'
print(uitvoer.format(a, b, c))
