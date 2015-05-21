import math

class Vector(object):
    """Represents a vector in 3-D space"""
    
    def __init__(self, n, waarde=0):
        self.n = n
        if waarde==0:
            self.vector = [0.0]*n
        elif isinstance(waarde, float) or isinstance(waarde, int):
            self.vector = [float(waarde)]*n
        else:
            self.vector = []
            for i in waarde:
                self.vector.append(float(i))
    
    def __str__(self):
        output = ""
        for i in list(range(0,self.n)):
            output += str(self.vector[i]) + "\n"
        return output
    
    def lincomb(self, other, alpha, beta):
        output = ""
        for i in list(range(0,len(self.vector))):
            element = alpha*self.vector[i]+beta*other.vector[i]
            output += str(element) + '\n'
        return output
    
    def scalar(self, alpha):
        output = ""
        for i in list(range(0,len(self.vector))):
            element = alpha*self.vector[i]
            output += str(element) + '\n'
        return output
    
    def inner(self, other):
        elementen = []
        for i in list(range(0,len(self.vector))):
            element = self.vector[i]*other.vector[i]
            elementen.append(element)
        output = sum(elementen)
        return output
    
    def norm(self):
        kwadraat = self.inner(self)
        output = math.sqrt(kwadraat)
        return output
    
    def GrammSchmidt(V):
        