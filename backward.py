import numpy as np

# Given data
x = np.array([1, 2, 3, 4, 5])
y = np.array([1, 8, 27, 64, 125])  # y = x³ উদাহরণ

n = len(x)
h = x[1] - x[0]

# Backward difference table তৈরি
diff = np.zeros((n, n))
diff[:,0] = y

for j in range(1, n):
    for i in range(j, n):
        diff[i][j] = diff[i][j-1] - diff[i-1][j-1]

# মান বের করার function
def backward_interpolate(x_val):
    p = (x_val - x[-1]) / h
    sum_val = y[-1]
    fact = 1
    p_term = 1

    for i in range(1, n):
        fact *= i
        p_term *= (p + (i-1))
        sum_val += (p_term * diff[-1][i]) / fact
    return sum_val

# Example: x=4.5 এ y এর মান বের করা
x_val = 4.5
print(f"Backward Interpolation Result y({x_val}) = {backward_interpolate(x_val)}")
