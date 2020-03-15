def ik_heb_gemoord(opdrachtenlijst, moordenaar):
    if moordenaar == opdrachtenlijst[0] and len(opdrachtenlijst) == 1:
        return moordenaar, opdrachtenlijst
    else:
        positie = opdrachtenlijst.index(moordenaar)
        if positie == len(opdrachtenlijst) - 1:
            opdrachtenlijst.pop(0)
        else:
            opdrachtenlijst.pop(positie + 1)


        positie = int(opdrachtenlijst.index(moordenaar))
        if positie == len(opdrachtenlijst) - 1:
            nieuw_slachtoffer = opdrachtenlijst[0]
        else:
            nieuw_slachtoffer = opdrachtenlijst[positie + 1]

        return nieuw_slachtoffer, opdrachtenlijst

def ik_ben_vermoord(lijst, slachtoffer):
    if lijst.index(slachtoffer) == len(lijst) - 1:
        nieuwe = lijst[0]
    else:
        nieuwe = lijst[lijst.index(slachtoffer) + 1]
    if len(lijst) != 1:
        lijst.remove(slachtoffer)
    return (nieuwe, lijst)

