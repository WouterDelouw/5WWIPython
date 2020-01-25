def volgend_collatz_getal(getal_n):
    if getal_n % 2 == 0:
        nieuw_getal = getal_n / 2
    else:
        nieuw_getal = getal_n * 3 + 1
    return int(nieuw_getal)



def collatz(getal_n):
    aantal = 1
    while getal_n != 1:
        aantal += 1
        getal_n = volgend_collatz_getal(getal_n)
    return aantal
