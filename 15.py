# Write a python program to find the sum of the series 1/2-2/3+3/4-4/5 + ... till n terms using function.

def find_s(n):
    sum = 0
    for i in range(1, n+1):
        if i % 2 == 0:
            sum -= (2/i)
        else:
            sum += (2/i)
    return sum
if __name__ == "__main__":
    n = int(input("Enter the number of terms: "))
    print(find_s(n))
