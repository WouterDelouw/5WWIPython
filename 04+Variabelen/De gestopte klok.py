# invoer
# vertrek thuis
h_vh = float(input('a: '))
m_vh = float(input('b: '))

# aankomst andrea
h_aa = float(input('c: '))
m_aa = float(input('d: '))

# vertrek andrea
h_va = float(input('e: '))
m_va = float(input('f: '))

# aankomst thuis
h_ah = float(input('g: '))
m_ah = float(input('h: '))

# berekeningen
vh = (h_vh * 60) + m_vh
aa = (h_aa * 60) + m_aa
va = (h_va * 60) + m_va
ah = (h_ah * 60) + m_ah

tijd_andrea = (va - aa)
tijd_huis = (ah - vh)
vertrek_andrea = tijd_huis + (720 - (720 * (tijd_huis / abs(tijd_huis))))
yy5 = tijd_andrea + (720 - (720 * (tijd_andrea / abs(tijd_andrea))))
enkele_trip = (vertrek_andrea - yy5) / 2
echte_tijd = va + enkele_trip

hour = echte_tijd // 60
echte_tijd_ = echte_tijd - 24
hour_ = hour - 12 + (12 * (echte_tijd_ / abs(echte_tijd_)))
minutes = echte_tijd % 60


# uitvoer
print(abs(int(hour_)))
print(int(minutes))
