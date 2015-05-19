lengte = input()

hekjes = 0

for i in list(range(0,int(lengte))):
    strook = input()
    for j in list(range(0,len(strook))):
        if strook[j]=='#':
            hekjes += 1

verf = hekjes*5

print('Om de hekjes in dit weiland te verven heb je ' + str(verf) + ' liter verf nodig')