lengtewoordenboek = int(input())

woordenboek = []
for i in list(range(0,lengtewoordenboek)):
    woord = input()
    woordenboek.append(woord)

def test(swype, woordenboek):
    lengteswype = len(swype)
    oplossing = '?'
    for element in woordenboek:
        lengteelement = len(element)
        n = 0
        for letter in list(range(0,lengteelement)):
            while n<lengteswype:
                while swype[n]!=element[letter]:
                    n += 1
        if n<lengteswype and swype[0]==element[0] and swype[lengteswype-1]==element[lengteelement-1]:
            oplossing = element
    return oplossing

aantalswypes = int(input())

for i in list(range(0,aantalswypes)):
    swype = input()
    print(test(swype, woordenboek))