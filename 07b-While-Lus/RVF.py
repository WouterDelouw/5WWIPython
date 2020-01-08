woord, bedrag, gegokte, som, letter = input('geef het woord: '), int(input('geef het gedraaid geldbedrag: ')), '', 0, input('geef een letter')
while letter in woord and not letter in gegokte:
    gegokte += letter
    som += bedrag
    letter = input('geef een letter')
print(som)
