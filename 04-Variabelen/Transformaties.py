# invoer

a = float(input('a: '))
b = float(input('b: '))

# berekeningen
f_b = str(int(4 + b))
f_a = str(int(-(-3 - a)))

print('f(x) = 2(x - 3)^2 + 4')
print('g(x) = 2(x - ' + f_a + ')^2 + ' + f_b)
