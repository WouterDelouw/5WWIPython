# invoer
dobbelsteen_1_a = int(input('aantal ogen dobbelsteen 1 aanvaller : '))
dobbelsteen_2_a = int(input('aantal ogen dobbelsteen 2 aanvaller : '))
dobbelsteen_3_a = int(input('aantal ogen dobbelsteen 3 aanvaller : '))
dobbelsteen_1_v = int(input('aantal ogen dobbelsteen 1 verdediger : '))
dobbelsteen_2_v = int(input('aantal ogen dobbelsteen 2 verdediger : '))

aantal_legers_aanvaller = 0
aantal_legers_verdediger = 0

# berekeningen: dobbelstenen op volgorde zetten
grootste_ogen_aanvaller = max(dobbelsteen_1_a, dobbelsteen_2_a, dobbelsteen_3_a)
tweede_ogen_aanvaller = (max(min(dobbelsteen_1_a, dobbelsteen_2_a), min(dobbelsteen_1_a, dobbelsteen_3_a), min(dobbelsteen_2_a, dobbelsteen_3_a)))
grootste_ogen_verdediger = max(dobbelsteen_1_v, dobbelsteen_2_v)
tweede_ogen_verdediger = min(dobbelsteen_1_v, dobbelsteen_2_v)

# winnaar berekenen
if grootste_ogen_verdediger >= grootste_ogen_aanvaller:
    aantal_legers_aanvaller += 1
else:
    aantal_legers_verdediger +=1
if tweede_ogen_verdediger >= tweede_ogen_aanvaller:
    aantal_legers_aanvaller += 1
else:
    aantal_legers_verdediger += 1

if aantal_legers_aanvaller != 1 and aantal_legers_verdediger != 1:
    print('aanvaller verliest',aantal_legers_aanvaller, 'legers, verdediger verliest', aantal_legers_verdediger,'legers')
elif aantal_legers_aanvaller == 1 and aantal_legers_verdediger != 1:
    print('aanvaller verliest',aantal_legers_aanvaller, 'leger, verdediger verliest', aantal_legers_verdediger,'legers')
elif aantal_legers_aanvaller != 1 and aantal_legers_verdediger == 1:
    print('aanvaller verliest',aantal_legers_aanvaller, 'legers, verdediger verliest', aantal_legers_verdediger,'leger')
elif aantal_legers_aanvaller == 1 and aantal_legers_verdediger == 1:
    print('aanvaller verliest',aantal_legers_aanvaller, 'leger, verdediger verliest', aantal_legers_verdediger,'leger')

