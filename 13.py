# Write a python to replace blank space with hypen in a given string.

def replace_blanks(string):
    return string.replace(' ', '-')
if __name__ == '__main__':
    string = input("Enter string : ")
    print(replace_blanks(string))