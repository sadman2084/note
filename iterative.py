# f(x) = x^3 - x - 1
# Iterative Method: x = g(x) = (x + 1) ** (1/3)

def g(x):
    return (x + 1) ** (1/3)   

x0 = 1.5        
tol = 1e-6      
max_iter = 100 

for i in range(max_iter):
    x1 = g(x0)
    if abs(x1 - x0) < tol:  
        print(f"main value {x1:.6f}")
        break
    x0 = x1
    
else:
    print("Iteration not possible")
