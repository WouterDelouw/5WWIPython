# invoer
a = int(input('a:'))
b = int(input('b:'))

# berekeningen
c = a + b
uitvoer = '{:>5d} + {:<5d} = {:d}'

# uitvoer
print(uitvoer.format(a, b, c))
print(uitvoer.format(10*a, 10*b, 10*c))
print(uitvoer.format(100*a, 100*b, 100*c))
print(uitvoer.format(1000*a, 1000*b, 1000*c))
print(uitvoer.format(10000*a, 10000*b, 10000*c))
