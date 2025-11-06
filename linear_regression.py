import numpy as np
import matplotlib.pyplot as plt
x=np.array([1,2,3])
y=np.array([2,4,6])
m=0
b=0
learning_rate=0.1
for i in range(1000):
    y_pred=m*x+b
    loss=np.mean((y-y_pred)**2)
    dm=(-2/len(x))*np.sum(x*(y-y_pred))
    db=(-2/len(x))*np.sum((y-y_pred))

    m=m-learning_rate*dm
    b=b-learning_rate*db
    if i%100==0:  
        print(f"Iteration {i}: m={m:.4f}, b={b:.4f}, Loss={loss:.4f}")
test=5
y_prediction=m*test +b
print(f"Prediction for {test} is {y_prediction:.4f}")

plt.scatter(x, y, color="red", label="Original data")
plt.plot(x, m*x + b, color="blue",label="Fitted line")
plt.title("Linear Regression Fit")
plt.xlabel("X")
plt.ylabel("Y")

