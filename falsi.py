import math
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
def f(x):
    return 3*x-x**2-1
def falsi(a,b,tol):
    while abs(b-a)>=tol:
        c = b - ((f(b)*(b-a)) / (f(a) - f(b)))
        if f(c)*f(a)<0:
            b=c
        elif f(c)*f(a)>0:
            a=c
        else:
            return c
    return c

a=0
b=1
tol=1e-6
solve=falsi(a,b,tol)
print("The root is approximately:",solve)


xs=np.linspace(a,b,100)
ys=[f(x) for x in xs]
sns.set(style="darkgrid")
plt.axhline(0,color='black',lw=.5)
plt.scatter(solve,f(solve),color='red')
plt.plot(xs,ys,color='blue',label='f(x)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title("bisection")
