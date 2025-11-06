import math
def func(x):
    return  3*x -math.cos(x)-1

def bisection(a, b, tolerance):
    while abs(b-a)/b>=tolerance:
        c=(a+b)/2
        if(func(c)*func(a) == 0):
            return c
        elif func(c)*func(a) > 0:
            a = c
        else:
            b = c
    print("ans is ",c)  
    return c

a,b,tolerance=map(float,input("enter a b and tolerance ").split())
if a > b:
    print("a is greater than b")
else:
    bisection(a, b, tolerance)


