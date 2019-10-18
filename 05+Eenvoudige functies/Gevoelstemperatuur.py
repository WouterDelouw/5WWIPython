# invoer
t = float(input('t :'))
w = float(input('w: '))

#13,12+0,6215T+(0,3965T−11,37)(3,6W)0,16
# berekeningen
gevoelstemperatuur = 13.12 + 0.6215 * t - 11.37 * pow(w, 0.16) + 0.3965 * t * pow(w, 0.16)

# uitvoer
print(gevoelstemperatuur)
