import math
class Vector():
    
    def __init__(self, n, i=0):
        if type(i)==list:
            self.vector = i
            self.n = n
        else:
            self.vector = [i]*n
            self.n = n
    
    def __str__(self):
        self.output = ""
        for i in range(0,self.n):
            self.output += str(self.vector[i]) + "\n"
        return self.output
    
    def scalar(self, alpha):
        return(Vector(self.n, list(map(lambda x: x *alpha, self.vector))))
    
    def inner(self, other):
        return sum(list(map(lambda x,y: x *y, self.vector, other.vector)))
    
    def norm(self):
        return math.sqrt(self.inner(self))
    
    def lincomb(self, other, alpha, beta):
        return Vector(self.n, list(map(lambda x,y: x+y, self.scalar(alpha).vector, other.scalar(beta).vector)))

def GrammSchmidt(V):
    V[0] = V[0].scalar(1/V[0].norm())
    basis_vectoren = [V[0]]
    for i in range(1, len(V)):
        basis =  V[i]
        for n in range(0,i):
            projectie = basis_vectoren[n].scalar(basis.inner(basis_vectoren[n]) / basis_vectoren[n].norm())
            basis = basis.lincomb(projectie,1,-1)
            basis = basis.scalar(1/basis.norm())
        basis_vectoren.append(basis)
    return(basis_vectoren)