import numpy as np

# Given data
x = np.array([1, 2, 3, 4, 5])
y = np.array([1, 8, 27, 64, 125])   # y = x³ উদাহরণ

n = len(x)
h = x[1] - x[0]

# Forward difference table তৈরি
diff = np.zeros((n, n))
diff[:,0] = y

for j in range(1, n):
    for i in range(n - j):
        diff[i][j] = diff[i+1][j-1] - diff[i][j-1]

# মান বের করার জন্য function
def forward_interpolate(x_val):
    p = (x_val - x[0]) / h
    sum_val = y[0]
    fact = 1
    p_term = 1

    for i in range(1, n):
        fact *= i
        p_term *= (p - (i-1))
        sum_val += (p_term * diff[0][i]) / fact
    return sum_val

# Example: x=2.5 এ y এর মান বের করা
x_val = 2.5
print(f"Forward Interpolation Result y({x_val}) = {forward_interpolate(x_val)}")
