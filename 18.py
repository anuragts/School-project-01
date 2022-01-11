# Write a python program to count the number of vowels from a text file.

def text_count(vowels):
    f = open("./test.txt", "r")
    object = f.read()
    object = object.lower()
    count = 0
    for i in object:
        if i in vowels:
            count += 1
    print(count)
    f.close()
if __name__ == "__main__":
    vowels = ['a', 'e', 'i', 'o', 'u']
    text_count(vowels)
