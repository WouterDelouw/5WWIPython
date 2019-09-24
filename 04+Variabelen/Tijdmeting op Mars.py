# invoer
aantal_sol = float(input('sol: '))


# berekeningen
een_sol = ( 60 * 60 * 24 ) + ( 39 * 60 ) + 35.244
d = (aantal_sol * een_sol) // ( 60 * 60 * 24 )
u = ((aantal_sol * een_sol) % ( 60 * 60 * 24 )) // ( 60 * 60 )
m = (((aantal_sol * een_sol) % ( 60 * 60 * 24 )) % ( 60 * 60 )) // 60
s = ((((aantal_sol * een_sol) % ( 60 * 60 * 24 )) % ( 60 * 60 )) % 60) % 60

# uitvoer
print(int(aantal_sol), 'sol =', int(d), 'dagen,',int(u), 'uren,', int(m), 'minuten en', int(s), 'seconden')
