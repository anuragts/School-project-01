# Write a python program to check if a given key exsists in a dictionary myDict or not.

def find_key(key, myDict):
    if key in myDict:
        print(f"Key {key} is present in the dictionary")
    else:
        print("Key Age is not present in the dictionary")

if __name__ == '__main__':
    myDict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
    key = str(input("Enter the key to check: "))
    find_key(key, myDict)
