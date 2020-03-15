def fruitstuk_toevoegen(fruitmand, toevoegfruit):



    nieuwe = fruitmand
    vorig = []
    for element in fruitmand:
        huidig = element
        if len(vorig) + 1 < len(huidig):
            nieuwe.insert(fruitmand.index(element), huidig)
            break

        elif len(element) == len(toevoegfruit):
            fruitmand[fruitmand.index(element)] = toevoegfruit
    return fruitmand

