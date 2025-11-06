def f(x, y):
    return x + y    
x0 = 0   
y0 = 1     
h = 0.1    
n = 5      

for i in range(n):
    y1 = y0 + h * f(x0, y0)
    x0 = x0 + h
    y0 = y1
    print(f"{x0:.2f}\t{y0:.4f}")
