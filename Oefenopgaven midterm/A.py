aantalvragen = int(input())

lijst = list(range(1, aantalvragen + 1))
for i in lijst:
    vraag = input()
    lengte = len(vraag)
    woorden = 1
    j = 0
    while j<lengte:
        if vraag[j]==' ':
            woorden += 1
        j += 1
    if woorden <= 4:
        print(vraag + ' krAh!')
    else:
        print('Crackers!')