def sgd_linear_regression(x, y, lr=0.01, epochs=100):
    w = 0.0 
    
    for epoch in range(epochs):
        
        for xi, yi in zip(x, y):
            y_pred = w * xi
            error = y_pred - yi
            grad = 2 * error * xi   # dL/dw
            w -= lr * grad
            
        
        if epoch % 10 == 0:
            print(f"Epoch {epoch:3d}: w = {w:.4f}, loss = {error:.4f}")
    
    return w

x = [1, 2, 3]
y = [2, 4, 6]

final_w = sgd_linear_regression(x, y, lr=0.01, epochs=100)
print("\nFinal learned weight:", final_w)