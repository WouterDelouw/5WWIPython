aantal_opeenvolgende = 0
aantal_tropisch = 0
stop = ''
while stop != 'stop':
    invoer = input('geef temperatuur')
    if invoer == 'stop':
        stop += invoer
    else:
        invoer = float(invoer)
        if invoer >= 30:
            aantal_opeenvolgende += 1
            aantal_tropisch += 1

        elif invoer >= 25:
            aantal_opeenvolgende += 1
        else:
            if aantal_opeenvolgende >= 5 and aantal_tropisch >= 3:
                invoer = 'stop'
            else:
                aantal_opeenvolgende = 0
                aantal_tropisch = 0

if aantal_opeenvolgende >= 5 and aantal_tropisch >= 3:
    uitvoer = 'hittegolf'
else:
    uitvoer = 'geen hittegolf'

print(uitvoer)


