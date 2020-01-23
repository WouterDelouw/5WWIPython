from math import sqrt, floor

# geeft aan of een getal een priemgetal is
# true, getal is een priemgetal, anders False

def is_priem(getal):
    i = 2
    while i <= floor(sqrt(n)) and n % i != 0:
         i += 1
    if i == floor(sqrt(n)) + 1:
        return True
    else:
        return False


aantal_gevraagd = int(input('aantal gevraagd: '))
som, aantal, n = 0, 0, 2
while aantal < aantal_gevraagd:
 if is_priem(n):
    som, aantal = som + n, aantal + 1
 n += 1
print(som)
