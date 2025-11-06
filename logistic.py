import numpy as np
import matplotlib.pyplot as plt


x=np.array([1,2,3,4,5,6,7])
y=np.array([0,0,0,0,1,1,1])


def sigmoid(z):
    return 1/(1+np.exp(-z))


m=0.0
b=0.0
L=0.1

for i in range(1000):
    z=m*x+b
    y_pred=sigmoid(z)

    dm=(-2/len(x))*np.sum(x*(y-y_pred))
    db=(-2/len(x))*np.sum((y-y_pred))

    m=m-L*dm
    b=b-L*db

    if i %100==0:
        print(f"m={m}, b={b}")

test=7
z=m*test+b
y_prediction=sigmoid(z)
print(f"Prediction for {test} is {y_prediction}")


xs=np.linspace(min(x)-1,max(x)+1,100)
plt.scatter(test,y_prediction,color='green')
plt.axhline(0.5,color='black')
ys=sigmoid(m*xs+b)
plt.plot(xs,ys,color='red')

