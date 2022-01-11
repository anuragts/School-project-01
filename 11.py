# Write a python program to find perfect number using loops

def find_perfect(n):
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    if sum == n:
        return True
    else:
        return False
if __name__ == '__main__':
    n = int(input("Enter a number: "))
    if find_perfect(n):
        print(f"{n} is a perfect number")
    else:
        print(f"{n} is not a perfect number")