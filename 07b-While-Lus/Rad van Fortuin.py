woord = input('woord: ')
bedrag = int(input('bedrag: '))
gegokte_letters = ''
geldsom = 0
letter = input('letter :')
while letter in woord and not letter in gegokte_letters:
    gegokte_letters += letter
    geldsom += bedrag
    letter = input('letter: ')
print(geldsom)
