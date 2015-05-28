from Vector import *

a = Vector(3, [2,8,-1.0])
b = Vector(3, [1,1,2])
c = a.norm()

print(c)

v0 = Vector(2,[3,1])
v1 = Vector(2,[2,2])
W = GrammSchmidt([v0,v1])

print(W[0])
print(W[1])
print(W[0].inner(W[1]))
print(W[0].norm())