x = int(input('geef een getal: '))
deelbaar = 0
nietdeelbaar = 0

if x == 1:
    uitvoer = ('geen priemgetal')
elif x == 2:
    uitvoer = ('een priemgetal')
else:
    for i in range(2, x):
        if x % i != 0:
            nietdeelbaar += 1
        else:
            deelbaar += 0

    if deelbaar != 0:
        uitvoer = ('geen priemgetal')
    else:
        uitvoer = ('een priemgetal')
print(x, 'is', uitvoer)
