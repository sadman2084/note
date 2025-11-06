# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# from sklearn.linear_model import LinearRegression
# from sklearn.preprocessing import PolynomialFeatures

# # Sample data (replace with your real dataset)
# data = {
#     'age': [1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5],
#     'length': [85, 120, 160, 190, 215, 230, 250, 265, 275]
# }
# df = pd.DataFrame(data)

# X = df[['age']]
# y = df['length']

# # Polynomial Features (degree 2 or 3)
# poly = PolynomialFeatures(degree=2)
# X_poly = poly.fit_transform(X)

# # Fit the model
# model = LinearRegression()
# model.fit(X_poly, y)

# # Predict
# y_pred = model.predict(X_poly)

# # Print equation
# coefs = model.coef_
# intercept = model.intercept_
# print(f"Model equation: y = {intercept:.2f} + {coefs[1]:.2f}x + {coefs[2]:.2f}x²")

# # Plot
# plt.scatter(X, y, color='blue', label='Actual Data')
# plt.plot(X, y_pred, color='red', label='Polynomial Fit (degree=2)')
# plt.xlabel('Age (years)')
# plt.ylabel('Length (mm)')
# plt.title('Polynomial Regression: Rui Fish Age vs Length')
# plt.legend()
# plt.grid(True)
# plt.show()

# Polynomial Regression without any external library (degree = 2)

# Sample data
age = [1, 2, 3, 4, 5]
length = [85, 160, 215, 250, 275]

n = len(age)

# Calculate all necessary summations
Σx = sum(age)
Σx2 = sum([x**2 for x in age])
Σx3 = sum([x**3 for x in age])
Σx4 = sum([x**4 for x in age])
Σy = sum(length)
Σxy = sum([age[i]*length[i] for i in range(n)])
Σx2y = sum([(age[i]**2)*length[i] for i in range(n)])

# Now solve the normal equations:
# a0*n + a1*Σx + a2*Σx² = Σy
# a0*Σx + a1*Σx² + a2*Σx³ = Σxy
# a0*Σx² + a1*Σx³ + a2*Σx⁴ = Σx²y

# Use manual matrix solution (Cramer's Rule)
# First calculate determinant D

D = (n*(Σx2*Σx4 - Σx3*Σx3)
     - Σx*(Σx*Σx4 - Σx2*Σx3)
     + Σx2*(Σx*Σx3 - Σx2*Σx2))

D1 = (Σy*(Σx2*Σx4 - Σx3*Σx3)
      - Σx*(Σxy*Σx4 - Σx3*Σx2y)
      + Σx2*(Σxy*Σx3 - Σx2*Σx2y))

D2 = (n*(Σxy*Σx4 - Σx3*Σx2y)
      - Σy*(Σx*Σx4 - Σx2*Σx3)
      + Σx2*(Σx*Σx2y - Σx2*Σxy))

D3 = (n*(Σx2*Σx2y - Σx3*Σxy)
      - Σx*(Σx*Σx2y - Σx2*Σxy)
      + Σy*(Σx*Σx3 - Σx2*Σx2))

a0 = D1 / D
a1 = D2 / D
a2 = D3 / D

print(f"Polynomial equation:")
print(f"y = {a0:.3f} + {a1:.3f}x + {a2:.3f}x²")

# Predict for a given age
test_age = 6
y_pred = a0 + a1*test_age + a2*(test_age**2)
print(f"\nPredicted length for age={test_age} years ≈ {y_pred:.2f} mm")
