hoogsteniveau = int(input())
niveaus = input()

genodigden = 0

def bereken_staan(genodigden):
    staan = genodigden + int(niveaus[0])
    for i in list(range(1,hoogsteniveau)):
        if staan>=i:
            staan += int(niveaus[i])
    return staan

def test(genodigden):
    staan = bereken_staan(genodigden)
    if staan>=hoogsteniveau:
        print(genodigden)
    else:
        genodigden += 1
        test(genodigden)

test(genodigden)