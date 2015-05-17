bericht = input()
codewoord = input()

lijst = list(range(0,len(bericht)))
for i in lijst:
    getal1 = ord(bericht[i])
    getal2 = ord(codewoord[i%len(codewoord)])
    uitkomst = ((getal1-getal2)%26)+97
    nieuw = chr(uitkomst)
    bericht = bericht[0:i] + nieuw + bericht[i+1:len(bericht)]

print(bericht)