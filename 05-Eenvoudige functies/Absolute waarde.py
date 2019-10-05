# invoer
x = float(input('x:'))
y = float(input('y:'))


# berekeningen
a = abs(abs(x)-abs(y))
b = abs(x - y)

uitvoer = '{:.4f} \N{LESS-THAN OR EQUAL TO} {:.4f}'



# uitvoer
print(uitvoer.format(a, b))
