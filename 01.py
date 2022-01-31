# Write a python program to check the number is prime or not.

def check_prime(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


if __name__ == '__main__':
    n = int(input("Enter a number: "))
    if check_prime(n):
        print(f"{n} is a prime number.")
    else:
        print(f"{n} is not a prime number.")