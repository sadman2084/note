
n = int(input("how many equations:"))
a = []
print("all row coff:")
for i in range(n):
    a.append(list(map(float, input(f"Row {i+1}: ").split())))
# Forward elimination
for i in range(n):
    # Make the diagonal element 1
    factor = a[i][i]
    for j in range(i, n+1):
        a[i][j] /= factor
    # Make the below rows 0
    for k in range(i+1, n):
        factor = a[k][i]
        for j in range(i, n+1):
            a[k][j] -= factor * a[i][j]

# Back substitution
x = [0] * n  

for i in range(n-1, -1, -1):   # last row থেকে first row পর্যন্ত
    total = 0
    for j in range(i+1, n):     # ইতিমধ্যেই solved variables যোগ
        total += a[i][j] * x[j]
    x[i] = a[i][n] - total      # current variable solve

print("Solution:", x)
