string_1 = str(input('geef eerste string: '))
string_2 = str(input('geef tweede string: '))
prefix = ''
suffix = ''
nieuwestring_1 = string_1
nieuwestring_2 = string_2
teller = 0

voor_of_achter = 0
for letter in string_1:

    if letter == string_2[teller]:
        if voor_of_achter == 0:
            prefix += letter
        else:
            suffix += letter
        nieuwestring_1 = nieuwestring_1.replace(letter, '')
        nieuwestring_2 = nieuwestring_2.replace(letter, '')
    else:
        voor_of_achter = 1
    teller += 1
if len(nieuwestring_1) > len(nieuwestring_2):
    nieuwestring_2 += (len(nieuwestring_1) - len(nieuwestring_2)) * ' '

elif len(nieuwestring_1) < len(nieuwestring_2):
    nieuwestring_1 += (len(nieuwestring_2) - len(nieuwestring_1)) * ' '



uitvoer = len(prefix) * ' ' + '┏' + nieuwestring_1 + '┓ \n' + prefix + '┫' + (max(len(nieuwestring_1), len(nieuwestring_2))) * ' ' + '┣' + suffix + '\n' + len(prefix) * ' ' + '┏' + nieuwestring_1 + '┓'
