# Write a python program to find last occurence of a character in a given string.

def last_occurence(n, ch):
    position = n.rfind(ch)
    if position == -1:
        print("Character not found")
    else:
        print(f"Last of position of the character '{ch}' in the string '{n}' is {position} ")

if __name__ == '__main__':
    n = input("Enter a string: ")
    ch = input("Enter a character: ")
    last_occurence(n, ch)
    