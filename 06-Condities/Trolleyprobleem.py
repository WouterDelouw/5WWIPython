# invoer
antwoord_1 = str(input('hendel trekken?: '))
antwoord_2 = str(input('dikzak van brug duwen?: '))
doden = 0
# berekeningen
if antwoord_1 == 'ja':
    if antwoord_2 == 'ja':
        doden += 2
    else:
        doden += 1
else:
    if antwoord_2 == 'ja':
        doden += 1
    else:
        doden = 5
print(doden)
# veel makkelijker
# if antwoord_1 != antwoord_2
#   doden = 1
#elif antwoord_1 == 'ja'




