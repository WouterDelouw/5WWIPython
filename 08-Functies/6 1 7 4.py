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
    string_1 = str(cijfer_1) + str(cijfer_2) + str(cijfer_3) + str(cijfer_4)
    string_2 = str(cijfer_4) + str(cijfer_3) + str(cijfer_2) + str(cijfer_1)
    return string_1, string_2




def verschil(oplopend, aflopend):
    uitkomst = int(oplopend) - int(aflopend)
    return str(uitkomst)



def kaprekar(startgetal):
    string = ''
    while int(startgetal) != 6174:
        splits_1, splits_2, splits_3, splits_4 = splits(startgetal)
        splits_1, splits_2, splits_3, splits_4 = oplopende_cijfers(splits_1, splits_2, splits_3, splits_4)
        aflopend_getal, oplopend_getal = op_af_getallen(splits_1, splits_2, splits_3, splits_4)
        verschil_verschil = verschil(oplopend_getal, aflopend_getal)
        startgetal = verschil_verschil
        if int(verschil_verschil) != 6174:
            string += str(oplopend_getal) + ' - ' + str(aflopend_getal) + ' = ' + verschil_verschil + '\n'
        else:
            string += str(oplopend_getal) + ' - ' + str(aflopend_getal) + ' = ' + verschil_verschil

    return string
