def graad(woord):
    graad = 0
    woordlijst = []
    woordlijst += woord

    for i in range(0, len(woordlijst) // 2):
        if woordlijst[i] == woordlijst[i + len(woordlijst) // 2]:
            graad += 1

    return graad
