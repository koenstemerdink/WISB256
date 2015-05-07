import math
import sys
import random

N = int(sys.argv[1])
L = float(sys.argv[2])

if len(sys.argv)==4:
    seed = float(sys.argv[3])
    random.seed(seed)

if len(sys.argv)<3:
    print('Use: estimate_pi.py N L')
#if L>1:
#    print('AssertionError: L should be smaller than 1')

def drop_needle(L):
    x0 = random.random()
    y0 = random.random()
    angle = random.vonmisesvariate(0,0)
    punt2 = (x0+L*math.cos(angle),y0+L*math.sin(angle))
    if punt2[0]<=0 or punt2[0]>=1:
        hit = True
    else:
        hit = False
    return hit

aantalhits = 0
for i in range(1,N):
    resultaat = drop_needle(L)
    if resultaat == True:
        aantalhits += 1

if L<=1:
    pi = (2*L)/(aantalhits/float(N))
else:
    pi = (2*L)/(aantalhits/float(N)-1)-(2*(math.sqrt(L**2-1)+math.asin(1/L)))/(aantalhits/float(N)-1)

print(str(aantalhits) + ' hits in ' + str(N) + ' tries')
print('Pi = ' + str(pi))