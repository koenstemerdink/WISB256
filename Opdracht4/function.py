import bisection
import math

root1 = bisection.findRoot(lambda x: x**2-2,-2,2,.0001)
print(root1)

root2 = bisection.findRoot(lambda x: math.sin(x),0,9,.0001)
print(root2)

root3 = bisection.findAllRoots(lambda x: x**2-2,-2,2,.0001)
print(root3)

root4 = bisection.findAllRoots(lambda x: math.sin(x),0,9,.0001)
print(root4)