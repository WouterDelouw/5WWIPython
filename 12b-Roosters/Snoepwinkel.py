from operator import itemgetter
def bereken_prijs(lijst):
    prijs = 0
    for i in range(len(lijst)):
        prijs += lijst[i][1]
    return prijs




def winkelbriefje(lijst):
    briefje = []
    for i in range(len(lijst)):
        briefje += [lijst[i][0]]
    return briefje



def sorteer(lijst):
    lijst.sort(key=itemgetter(1))
    return lijst

