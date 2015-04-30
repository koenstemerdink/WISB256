import sys
import time

T1 = time.perf_counter()

N = int(sys.argv[1])

lijst = list(range(2,N))

for mini in lijst:
    for getal in lijst:
        if (getal%mini==0 and getal!=mini):
            lijst.remove(getal)

#print(lijst)

primes = open(sys.argv[2], 'w')

for getal in lijst:
    primes.write(str(getal) + '\n')

T2 = time.perf_counter()

print('Found', len(lijst), 'Prime numbers smaller than', N, 'in', T2-T1, 'sec.')