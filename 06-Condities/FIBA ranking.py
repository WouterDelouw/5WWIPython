# invoer
thuisploeg = float(input('aantal punten thuisploeg: '))
uitploeg = float(input('aantal punten uitploeg: '))

# berekeningen
if thuisploeg > uitploeg:
    verschil = thuisploeg - uitploeg
    if verschil < 10:
        punten_thuisploeg = 600
        punten_uitploeg = 400
    elif 10 <= verschil < 20:
        punten_thuisploeg = 700
        punten_uitploeg = 300
    else:
        punten_thuisploeg = 800
        punten_uitploeg = 200
else:
    verschil = uitploeg - thuisploeg
    if verschil < 10:
        punten_uitploeg = 600
        punten_thuisploeg = 400
    elif 10 <= verschil < 20:
        punten_uitploeg = 700
        punten_thuisploeg = 300
    else:
        punten_uitploeg = 800
        punten_thuisploeg = 200

punten_uitploeg += 70
punten_thuisploeg -= 70

punten_uitploeg = float(punten_uitploeg)
punten_thuisploeg = float(punten_thuisploeg)

uitvoer_thuisploeg = 'thuisploeg: {:.2f}'
uitvoer_uitploeg = 'uitploeg: {:.2f}'

# uitvoer

print(uitvoer_thuisploeg.format(punten_thuisploeg))
print(uitvoer_uitploeg.format(punten_uitploeg))
