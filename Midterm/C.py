n = int(input())

if n==0 or n==1 or n==2:
    uitkomst = 0
elif n==3:
    uitkomst = 1
elif n>3:
    def G(x):
        if x==0:
            return 0
        elif x==1:
            return 0
        elif x==2:
            return 0
        elif x==3:
            return 1
        else:
            return G(x-1)+G(x-2)+G(x-3)+G(x-4)
    uitkomst = G(n)

print(uitkomst)