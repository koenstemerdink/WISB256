import sys
import time
import math

N = int(sys.argv[1])
priemgetallen = open(sys.argv[2], 'w')
T1 = time.perf_counter()
aantal = 0

lijst = list(range(2,N))
lijst2 = list(range(3,int(math.sqrt(N)),2))
lijst2.insert(0,2)

for getal2 in lijst2:
    for getal in lijst[(getal2**2)-2:N-1]:
        if (getal%getal2==0 and getal!=getal2):
            lijst[getal-2]=0

for getal in lijst:
    if getal!=0:
        priemgetallen.write(str(getal) + '\n')
        aantal += 1

T2 = time.perf_counter()

print('Found', str(aantal), 'Prime numbers smaller than', N, 'in', T2-T1, 'sec.')