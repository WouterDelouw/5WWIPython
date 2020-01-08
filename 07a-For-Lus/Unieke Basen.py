# invoer
aantal_basen = int(input('hoeveel basen worden ingelezen?: '))
basen, uitvoerbase, meervoud = '', '', ''
aantal_verschillende = 0

a_base, t_base, g_base, c_base = 0, 0, 0, 0

# berekeningen
for i in range(aantal_basen):
    basen += input('geef base: ')

for letter in basen:
    if letter == 'A':
        a_base += 1
    elif letter == 'T':
        t_base += 1
    elif letter == 'G':
        g_base += 1
    else:
        c_base += 1


if a_base > 0:
    aantal_verschillende += 1
    uitvoerbase += 'A '
else:
    aantal_verschillende += 0
    uitvoerbase += ''

if c_base > 0:
    aantal_verschillende += 1
    uitvoerbase += 'C '
else:
    aantal_verschillende += 0
    uitvoerbase += ''

if g_base > 0:
    aantal_verschillende += 1
    uitvoerbase += 'G '
else:
    aantal_verschillende += 0
    uitvoerbase += ''

if t_base > 0:
    aantal_verschillende += 1
    uitvoerbase += 'T '
else:
    aantal_verschillende += 0
    uitvoerbase += ''

if aantal_verschillende == 1:
    meervoud += ' soort base: '
else:
    meervoud += ' verschillende soorten basen: '

# uitvoer
print('De DNA-keting bevat ' + str(aantal_verschillende)  + meervoud + uitvoerbase)
