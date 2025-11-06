import numpy as np
import matplotlib.pyplot as plt
def f(x):
    return np.exp(-x)*(3.2*np.sin(x) -0.5*np.cos(x))

a=3
b=4
eps_step=0.001
eps_abs=0.001

for i in range(1000):
    if abs(b-a)/2>eps_step or abs(f((a+b)/2))>eps_abs:
        c=(a+b)/2
        print(f"Iteration {i+1}: a={a:.2f}, b={b:.2f}, c={c:.5f}, f(c)={f(c):.5f}")
        if( f(a)*f(c)<0):
            b=c
        elif ( f(a)*f(c)>0):
            a=c
        else:
            print(f"Root found at x={c}")

x=np.linspace(3,4,400)
plt.plot(x,f(x))
plt.scatter(c,f(c),color='red')
plt.title("Bisection Method Root")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.show()