from math import sqrt

def binnen_of_buiten(middelpunt, random, xy):
    straal = sqrt((middelpunt[0] - random[0])**2 + (middelpunt[1] - random[1])**2)
    afstand = sqrt((middelpunt[0] - xy[0])**2 + (middelpunt[1] - xy[1])**2)
    if straal > afstand:
        positie = 'binnen'
    elif straal == afstand:
        positie = 'op'
    else:
        positie = 'buiten'
    uitvoer = (positie, afstand)
    return uitvoer

