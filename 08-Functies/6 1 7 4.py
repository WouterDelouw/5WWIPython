def splits(getal):
    teller = 0
    for letter in str(getal):
        teller += 1
        if teller == 1:
            getal_1 = int(letter)
        elif teller == 2:
            getal_2 = int(letter)
        elif teller == 3:
            getal_3 = int(letter)
        elif teller == 4:
            getal_4 = int(letter)

    return getal_1, getal_2, getal_3, getal_4



def oplopende_cijfers(getal_1, getal_2, getal_3, getal_4):
    digit_1 = min(getal_1, getal_2, getal_3, getal_4)
    digit_4 = max(getal_1, getal_2, getal_3, getal_4)
    digit_2 = min(max(getal_1, getal_2), max(getal_1, getal_3), max(getal_1, getal_4), max(getal_2, getal_3), max(getal_2, getal_4), max(getal_3, getal_4))
    digit_3 = getal_1 + getal_2 + getal_3 + getal_4 - digit_1 - digit_2 - digit_4

    return digit_1, digit_2, digit_3, digit_4




def op_af_getallen(cijfer_1, cijfer_2, cijfer_3, cijfer_4):
    string_2 = str(cijfer_4) + str(cijfer_3) + str(cijfer_2) + str(cijfer_1)
    string_1 = str(cijfer_1) + str(cijfer_2) + str(cijfer_3) + str(cijfer_4)
    return string_1, string_2




def verschil(aflopend, oplopend):
    uitkomst = int(aflopend) - int(oplopend)
    ret = str(aflopend) + ' - ' + str(oplopend) + ' = ' +  str(uitkomst)
    return str(uitkomst)




def kaprekar(begingetal):
    while uitvoer != int(6174):
        uitvoer = verschil(oplopende_cijfers(splits(begingetal)))
        return (str(max(oplopende_cijfers(splits(begingetal)))) + ' - ' + (str(min(oplopende_cijfers(splits(begingetal)))) + ' = ' + str(uitvoer)
        begingetal = 0
        begingetal += uitvoer



print(kaprekar(int(input('getal: '))))
