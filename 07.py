# Write a python program to calculate the sum of the series 1**2 + 2**2 + 3**2 + ... + n**2 using for loop.

def sum_of_series(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i ** 2
    return sum
n = int(input("Enter the number: "))
if __name__ == '__main__':
    print(sum_of_series(n))
