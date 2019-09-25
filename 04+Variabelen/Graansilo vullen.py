# invoer
b = float((input('breedte: ')))
l = float((input('lengte: ')))
c = float((input('kubieke meter: ')))
r = float((input('straal: ')))
h = float((input('hoogte: ')))
pi = 3.14159265359

# berekeningen
m = float((b * l * c) / 10000)
een_silo = float(r**2 * pi * h)
aantal_silos = (m // een_silo) + 1
hoogte_silo = float((m % een_silo) / (r**2 * pi))

# uitvoer
print(int(aantal_silos))
print(hoogte_silo)

