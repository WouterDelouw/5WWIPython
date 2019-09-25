# invoer
t = float(input('tijd: '))

# berekeningen
c = 299792458
n = 1.000277
d = float((c * t * 10**-9) / (2 * n))

# uitvoer
print(d, 'meter')


