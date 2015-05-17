import math

vuurkracht = int(input())
zwaartekracht = int(input())
afstand = int(input())

hoek = (0.5)*math.asin((zwaartekracht*afstand)/(vuurkracht**2))

print("{0:.2f}".format(hoek))