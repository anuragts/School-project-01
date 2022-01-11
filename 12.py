# Write a python program to find roots of a Quadratic Equation.


from cmath import sqrt as s
def find_root(a,b,c):
    d = b**2 - 4*a*c
    if d < 0:
        print(f"No real roots")
    elif d == 0:
        root = (-b + s(d))/(2*a)
        print(f"One real root: {root}")
    else:
        root_1 = (-b + s(d))/(2*a)
        root_2 = (-b - s(d))/(2*a)
        print(f"Two real roots:{ root_1, root_2}")
    
if __name__ == '__main__':
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    c = float(input("Enter c: "))
    find_root(a,b,c)