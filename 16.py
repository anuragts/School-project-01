# Write a python program to print the series 1,9,17,33,49,73,97 ... till n terms ,using function.

def print_series(n):
    element = 0;
    for i in range(1,n+1):
        element = 0;
        if(i % 2 == 0):
            element = 2 * i * i + 1;
        else:
            element = 2 * i * i - 1;
        print(element,end= ", ");
if __name__ == "__main__":
    n = int(input("Enter the number of terms: "))
    print_series(n)

