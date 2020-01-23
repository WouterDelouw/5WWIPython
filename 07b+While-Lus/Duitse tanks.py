serienummer_1 = int(input('geef serienummer: '))
grootste = serienummer_1
stop = ''
nummer = 0
aantal = 1
while stop != 'stop':
    nummer = int(input('geef serienummer: '))
    if nummer > 0:
        grootste = max(grootste, nummer)
        aantal += 1
    else:
        stop += 'stop'

t = (((aantal + 1) * grootste) / aantal) -1

uitvoer = 'Het aantal geproduceerde tanks wordt geschat op {:.0f}.'
print(uitvoer.format(t))

