# invoer
loon = float(input('geef het loon: '))

# berekeningen

#  RSZ aftrekken
rsz = loon * 0.1307
loon_2 = loon - rsz

# lage lonen eruit halen en de schijven opvullen
if loon_2 <= 8860.00:
    totale_voorheffing = 0.000
    loon_3 = loon_2
else:
    if loon_2 >= 40480.01:
        schijf_1 = 13250.00
        schijf_2 = 10140.00
        schijf_3 = 17090.00
        schijf_4 = loon_2 - (schijf_1 + schijf_2 + schijf_3)
    elif loon_2 < 40480.01 and loon_2 > 23390.00:
        schijf_1 = 13250.00
        schijf_2 = 10140.00
        schijf_3 = loon_2 - (schijf_1 + schijf_2)
        schijf_4 = 0.00
    elif loon_2 < 23390.01 and loon_2 > 13250.00:
        schijf_1 = 13250.00
        schijf_2 = loon_2 - schijf_1
        schijf_3 = 0.00
        schijf_4 = 0.00
    else:
        schijf_1 = loon_2
        schijf_2 = 0.00
        schijf_3 = 0.00
        schijf_4 = 0.00

    belasting_schijf_1 = (schijf_1 - 8860.00) * 0.25
    belasting_schijf_2 = schijf_2 * 0.40
    belasting_schijf_3 = schijf_3 * 0.45
    belasting_schijf_4 = schijf_4 * 0.50
    totale_voorheffing = (belasting_schijf_1 + belasting_schijf_2 + belasting_schijf_3 + belasting_schijf_4)
    loon_3 = loon_2 - totale_voorheffing

#  maandloon berekenen
maandloon_netto = loon_3 / 12

#  uitvoer creeren
uitvoer_1 = '+ bruto jaarsalaris' + '{:>11.2f}'
uitvoer_2 = '- rsz' + '{:>25.2f}'
uitvoer_3 = '- voorheffing' + '{:>17.2f}'
uitvoer_4 = '=============================='
uitvoer_5 = '+ netto jaarsalaris' + '{:>11.2f}'
uitvoer_6 = '+ netto maandsalaris' + '{:>10.2f}'

# uitvoer doen
print(uitvoer_1.format(loon))
print(uitvoer_2.format(rsz))
print(uitvoer_3.format(totale_voorheffing))
print(uitvoer_4)
print(uitvoer_5.format(loon_3))
print(uitvoer_6.format(maandloon_netto))
