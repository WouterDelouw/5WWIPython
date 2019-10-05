# invoer
seconden = int(input('seconden: '))

# berekeningen
dagen = str(int(seconden // 86400))
u = str((seconden % 86400) // 3600)
m = str(((seconden % 86400) % 3600) // 60)
s = str((((seconden % 86400) % 3600) % 60))

# uitvoer
print(dagen + 'd ' + u + ':' + m + ':' + s)
