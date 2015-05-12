def findRoot(f,a,b,epsilon):
    if f(a)>f(b):
        c=a
        a=b
        b=c
    
    m = (a+b)/2
    
    if abs(b-a)<=epsilon:
        return m
    
    if f(m)<=0:
        return findRoot(f,m,b,epsilon)
    else:
        return findRoot(f,a,m,epsilon)

def findAllRoots(f,a,b,epsilon):
    nulpunten = []
    i=a
    while i<b:
        if (f(i)<=0 and f(i+epsilon)>=0) or (f(i)>=0 and f(i+epsilon)<=0):
            nul = findRoot(f,i,i+epsilon,epsilon)
            nulpunten.append(nul)
        i += epsilon
    return nulpunten