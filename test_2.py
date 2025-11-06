import numpy as np
import matplotlib.pyplot as plt
def f(t,y):
    return y-0.5*np.exp(t/2)*np.sin(5*t)+5*np.exp(t/2)*np.cos(5*t)
y=0
h=[0.1,0.05,0.01,0.005,0.001]
t=0
for i in range(5):
    t=t+1
    for j in range(5):
        y1=y+h[j]*f(t,y)
        y=y1
        print(f"h={h[j]} , t={t} , y(euler)={y1:.2f} , y(exact)={np.exp(t/2)*np.sin(5*t):.2f}")


plt.grid(True)
x=np.linspace(0,5,100)
plt.plot(x,np.exp(x/2)*np.sin(5*x),'k-',label="Exact solution")
plt.show()