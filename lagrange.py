def lagrange_interpolation(x, y, xp):
    n = len(x)
    yp = 0

    for i in range(n):
        p = 1
        for j in range(n):
            if i != j:
                p = p * (xp - x[j]) / (x[i] - x[j])
        yp = yp + p * y[i]
    
    return yp


# Example Data
x = [0, 1, 2, 3]
y = [1, 2, 0, 5]

xp = 2.5   # যে পয়েন্টে আমরা f(x) বের করব

yp = lagrange_interpolation(x, y, xp)

print(f"f({xp}) = {yp}")
