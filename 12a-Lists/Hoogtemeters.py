def hoogtemeters(lijst):
    resultaat = []

    for i in range(0, len(lijst) - 1):
        resultaat.append(lijst[i + 1] - lijst[i])

    return resultaat




def dalen_en_stijgen(lijst):
    dalen = 0
    stijgen = 0
    for meter in lijst:
        if meter > 0:
            stijgen += meter
        elif meter < 0:
            dalen += abs(meter)
    return (dalen, stijgen)
