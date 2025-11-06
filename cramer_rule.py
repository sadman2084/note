import numpy as np

# coefficient matrix (A)
A = np.array([[2, -1, 5],
              [3, 2, 2],
              [1, 3, 3]])

# constant matrix (B)
B = np.array([8, 14, 14])

# determinant of A
D = np.linalg.det(A)

if D == 0:
    print("No unique solution (determinant = 0)")
else:
    n = A.shape[0]
    X = np.zeros(n)
    for i in range(n):
        Ai = np.copy(A)
        Ai[:, i] = B      # Replace i-th column by B
        Di = np.linalg.det(Ai)
        X[i] = Di / D
    print("Solutions:")
    for i in range(n):
        print(f"x{i+1} = {X[i]}")
