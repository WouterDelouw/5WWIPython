def volgende_rij(vorige_rij):
    volgenderij = []
    for i in range(len(vorige_rij) - 1):
        if vorige_rij[i] == vorige_rij[i + 1]:
            volgenderij += vorige_rij[i]
        elif (vorige_rij[i] == 'G' and vorige_rij[i + 1] == 'R') or (vorige_rij[i] == 'R' and vorige_rij[i + 1] == 'G'):
            volgenderij += 'Y'
        elif (vorige_rij[i] == 'Y' and vorige_rij[i + 1] == 'R') or (vorige_rij[i] == 'R' and vorige_rij[i + 1] == 'Y'):
            volgenderij += 'G'
        elif (vorige_rij[i] == 'Y' and vorige_rij[i + 1] == 'G') or (vorige_rij[i] == 'G' and vorige_rij[i + 1] == 'Y'):
            volgenderij += 'R'
    return volgenderij


def driehoek(onderste_rij):
    lijst = [onderste_rij]
    nieuwe_rij = onderste_rij
    for i in range(len(onderste_rij) - 1):
        nieuwe_rij = volgende_rij(nieuwe_rij)
        lijst += [nieuwe_rij]
    return lijst


def kleuren(driehoek):
    G, R, Y = 0, 0, 0
    for i in range(len(driehoek)):
        G += driehoek[i].count('G')
        R += driehoek[i].count('R')
        Y += driehoek[i].count('Y')
    return G, R, Y
