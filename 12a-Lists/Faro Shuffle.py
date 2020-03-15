def nieuw_kaartspel(kleuren, waarden):
    nieuwe_lijst =[]
    for i in range(len(kleuren)):
        for j in range(len(waarden)):
            nieuwe_lijst += [str(kleuren[i]) + str(waarden[j])]
    return nieuwe_lijst

def splits_kaartspel(lijst):
    helft = len(lijst) // 2
    nieuw = (lijst[0:helft], lijst[helft:len(lijst)])
    return nieuw


def faro_shuffle(lijst_1, lijst_2):
    nieuw = []
    if len(lijst_2) == 1 and len(lijst_1) != 1:
        nieuw = lijst_2
    elif len(lijst_2) == len(lijst_1):
        for i in range(len(lijst_2)):
            nieuw.extend([lijst_1[i], lijst_2[i]])
    else:
        for i in range(len(lijst_1)):
            nieuw.extend([lijst_1[i], lijst_2[i]])
        nieuw.append(lijst_2[i + 1])
    return nieuw

