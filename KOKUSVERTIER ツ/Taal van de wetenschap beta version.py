s_1 = str(input('geef eerste string: '))
s_2 = str(input('geef tweede string: '))
string_1 = []
string_2 = []
string_1 += s_1
string_2 += s_2

prefix = ''
suffix = ''

nieuwestring_1 = string_1
nieuwestring_2 = string_2

teller = 0
grens = min(len(string_1), len(string_2))
stop = False
for i in range(0, grens):
    if string_1[i] == string_2[i] and stop != True:
        prefix += string_1[i]
        nieuwestring_1 = nieuwestring_1.pop(i)
        nieuwestring_2 = nieuwestring_2.pop(i)
    else:
        stop = True


string_1.reverse()
string_2.reverse()

stop = False
for i in range(0, grens):
    if string_1[i] == string_2[i] and stop != True:
        suffix += string_1[i]
        nieuwestring_1 = nieuwestring_1.pop(-(i + 1))
        nieuwestring_2 = nieuwestring_2.pop(-(i + 1))
    else:
        stop = True

prefix_g = prefix
suffix_g = ''
for letter in suffix:
    suffix_g = letter + suffix_g
nieuwestring_1.reverse(), nieuwestring_2.reverse()
nieuwestring_1_g = ''
for letter in nieuwestring_1:
    nieuwestring_1_g = letter + nieuwestring_1_g

nieuwestring_2_g = ''
for letter in nieuwestring_2:
    nieuwestring_2_g = letter + nieuwestring_2_g


print(prefix_g, nieuwestring_1_g, nieuwestring_2_g, suffix_g)

#uitvoer = len(prefix) * ' ' + '┏' + nieuwestring_1 + '┓ \n' + prefix + '┫' + (max(len(nieuwestring_1), len(nieuwestring_2))) * ' ' + '┣' + suffix + '\n' + len(prefix) * ' ' + '┗' + nieuwestring_1 + '┛'
