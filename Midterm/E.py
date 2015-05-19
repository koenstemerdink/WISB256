som = str(input()).split()

uitkomst = 0

def test_operaties(som):
    for i in list(range(0,len(som))):
        if som[i]=='+' or som[i]=='-' or som[i]=='*' or som[i]=='/':
            test = True
    if Test!=True:
        Test = False

while test_operaties(som)==True:
    n = 0
    while n==0:
        for i in list(range(0,len(som))):
            if som[i]=='+' or som[i]=='-' or som[i]=='*' or som[i]=='/':
                subuitkomst = eval(som[i-2] + som[i] + som[i-1])

for i in list(range(0,len(som))):
    if som[i]=='+' or som[i]=='-' or som[i]=='*' or som[i]=='/':
        subuitkomst = eval(som[i-2] + som[i] + som[i-1])
        som.remove(som[i-1])
        som.remove(som[i])
        som.remove(som[i+1])

uitkomst = eval(som[0] + som[2] + som[1])

print("{0:.3f}".format(float(uitkomst)))