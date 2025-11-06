def f(x, y):
    return x + y  

h = 0.1

x = [0, 0.1, 0.2, 0.3]
y = [1, 1.11, 1.242, 1.399]  


y_pred = y[0] + (4*h/3)*(2*f(x[1], y[1]) - f(x[2], y[2]) + 2*f(x[3], y[3]))

y_corr = y[2] + (h/3)*(f(x[2], y[2]) + 4*f(x[3], y[3]) + f(x[3]+h, y_pred))

print("Predicted y =", y_pred)
print("Corrected y =", y_corr)
