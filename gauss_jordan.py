import numpy as np
def gauss_jordan(A, b):
    n = len(b)
    A = A.astype(float)
    b = b.astype(float)
    M = np.hstack([A, b.reshape(-1, 1)])

    for i in range(n):
        # Make pivot = 1
        M[i] = M[i] / M[i][i]
        for j in range(n):
            if i != j:
                M[j] = M[j] - M[j][i] * M[i]
    return M


A = np.array([[2,3,-1], [4,4,-3], [-2,3,-2]], float)
b = np.array([5,3,1], float)
solution = gauss_jordan(A, b)
print("Solution (Gauss-Jordan):", solution)



# import numpy as np
# def g(a,b):
#       n=len(b)
#       a=a.astype(float)
#       b=b.astype(float)
#       m=np.hstack([a,b.reshape(-1,1)])

#       for i in range(n):
#             m[i]=m[i]/m[i][i]
#             for j in range(n):
#                   if i!=j:
#                         m[j]=m[j] -m[j][i]*m[i]

#       return m


# a=[]
# b=[]
# n =int(input("Enter number of equations: "  ))

# for i in range(n):
#     a.append(list(map(int,input(f"Enter coefficients of equation {i+1} separated by space: ").split())))
# for i in range(n):
#         b.append(float(input(f"Enter constant term of equation {i+1}: ")))


# a=np.array(a,float)
# b=np.array(b,float)
# solve=g(a,b)

# print(solve)


    
