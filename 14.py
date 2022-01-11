# Write a python program to print the series 2,15,41,80,132,197 ... till n terms using funtion.

def series(n):
    element = 0
    for i in range(1, n + 1):
        element = (13 * i * (i - 1)) / 2 + 2
        print(int(element), ", ", end = "")

if __name__ == '__main__':
    n = int(input("Enter the number of terms: "))
    series(n)
