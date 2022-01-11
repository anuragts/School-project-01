# Write a python program to accept  a character from user and print whether a character is an alphabet , digit or any other character. 

def check(n):
    if n.isalpha():
        print("Alphabet")
    elif n.isdigit():
        print("Digit")
    else:
        print("Other")
n = input("Enter a character: ")
if __name__ == "__main__":
    check(n)