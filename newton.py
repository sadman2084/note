import math

def f(x):
    return 3*x - math.cos(x) - 1 
def df(x):
    return 3 + math.sin(x) 

def Newton_Raphson(x0, iteration):

    print("initial guess, x0: ",x0)
    
    for i in range(1, iteration+1):
        fx = f(x0)
        dfx = df(x0)

        if dfx == 0:
            print("Zero derivative, Method fails.")

        x1 = x0 - fx/dfx

        print(f"Step-{i}: x = {x1:.6f}, f(x) = {f(x1):.6f}")

        x0 = x1

    return x1


root = Newton_Raphson(x0=0,iteration=10)
print("the root is: ",root)