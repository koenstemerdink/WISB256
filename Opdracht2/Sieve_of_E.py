import sys
import time

N = int(sys.argv[1])

T1 = time.perf_counter()

lijst = list(range(2,N))

for mini in lijst:
    for getal in lijst:
        if (getal%mini==0 and getal!=mini):
            lijst.remove(getal)

T2 = time.perf_counter()

primes = open(sys.argv[2], 'w')

for getal in lijst:
    primes.write(str(getal) + '\n')

print('Found', len(lijst), 'Prime numbers smaller than', N, 'in', T2-T1, 'sec.')