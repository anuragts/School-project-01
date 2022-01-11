# Write a program to print Fibbonacci series up to n terms.

def Fibbonacci(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()
n = int(input("Enter the number of terms: "))
if __name__ == '__main__':
    Fibbonacci(n)