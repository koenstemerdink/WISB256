getal = input()

if getal[0]!='U':
    aantal = int(getal)
    bericht = 'Ug'
    for i in list(range(1,aantal)):
        bericht = bericht + ' ug'
    bericht = bericht + '!'
    print(bericht)
else:
    bericht = 1
    for j in list(range(0,len(getal))):
        if getal[j]==' ':
            bericht += 1
    print(bericht)