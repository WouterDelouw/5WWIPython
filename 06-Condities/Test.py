getal = int(input('geef getal: '))

if getal < 0:
    if getal % 2 == 0:
        print('negetief even getal')
    else:
        print('negatief oneven getal')
elif getal > 0:
    if getal % 2 == 0:
        print('positief even getal')
    else:
        print('positief noeven getal')

print('tot ziens')
