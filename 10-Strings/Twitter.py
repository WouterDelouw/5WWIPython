tekst = str(input('geef een stukje tekst met hashtags: '))
woord =''
onthoud_woord = 0
nieuw = ''
for letter in tekst:
    if onthoud_woord == 1:
        woord += letter

    if letter == '#':
        onthoud_woord = 1
    elif letter == ' ':
        onthoud_woord = 0

for letter in woord:
    if letter == ' ':
        nieuw += '\n'
    else:
        nieuw += letter

print(nieuw)





