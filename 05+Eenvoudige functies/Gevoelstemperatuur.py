# invoer
t = float(input('t :'))
w = float(input('w: '))

# berekeningen
gevoelstemperatuur = float(13.12 + 0.6215 * t + (0.3965 * t - 11.37)*(3.6 * w)**0.16)

# uitvoer
print(gevoelstemperatuur)
