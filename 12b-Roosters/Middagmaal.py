def dagprijs(bestelling):
    prijs = 0
    ran = int(len(bestelling) / 2)
    for i in range(ran):
        if bestelling[2 * i] == 'soep':
            prijs += (bestelling[2 * i + 1] * 1.7)
        elif bestelling[2 * i] == 'vieruurtje':
            prijs += (bestelling[2 * i + 1] * 2.3)
        elif bestelling[2 * i] == 'middagmaal':
            prijs += (bestelling[2 * i + 1] * 5.3)
    round(prijs, 2)
    return prijs




def weekprijs(bestelling):
    totaal = 0
    for i in range(len(bestelling)):
        totaal += dagprijs(bestelling[i])
    return totaal
