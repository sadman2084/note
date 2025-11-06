import math

def g(x):
    return (math.cos(x) + 1) / 3      # x = g(x)  ⇒  root ≈ 0.607

def fixed_point(x0, tol=1e-6, max_iter=100):
    x_old = x0
    for i in range(1, max_iter + 1):
        x_new = g(x_old)

        # ➡️ কনভার্জেন্স টেস্ট: পুরোনো আর নতুনের পার্থক্য ছোট?
        if abs(x_new - x_old) < .0001:
            print(f"Converged after {i} iterations")
            return x_new

        x_old = x_new   # না হলে লুপ চালিয়ে যাও

    # লিমিট পেরিয়ে গেলে সাবধানবাণী
    print("Warning: Max iterations reached—may not have converged!")
    return x_new

# ---------- driver ------------
x0 = 0.5
root = fixed_point(x0, tol=1e-10)    # tighter tol = 1e‑10
print(f"Approximate root ≈ {root:.10f}")
