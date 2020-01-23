# invoer
aantal = int(input('geef het aantal lifters: '))
uitvoer = 0
lifter_1 = float(input('geef de score: '))
hoogste = lifter_1
teller = 0
for i in range(int(round(aantal / 2, 0)) - 1):
    lifter = float(input('geef de score: '))
    hoogste = max(hoogste, lifter)

for i in range(int(round(aantal / 2, 0)) - 1):
    lifter = float(input('geef de score: '))
    teller += 1
    if teller == i:
        uitvoer += lifter
    elif lifter > hoogste:
        uitvoer += lifter

print(uitvoer)

