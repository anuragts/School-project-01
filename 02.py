# Write a python program to check whether the number is palindrome or not.

def check_palindrome(num):
    num = str(num)
    return num == num[::-1]
num = int(input("Enter a number: "))
if __name__ == '__main__':
    if check_palindrome(num):
        print("The number is palindrome")
    else:
        print("The number is not palindrome")