r = int(input('geef getal tussen 1 en 100: '))
maximum = (100 // r) + 1
uitkomst = 0
for i in range(1, maximum):
    uitkomst += (i * r)
print(uitkomst)
