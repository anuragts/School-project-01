# Read a text file and display the number of vowels/Consonants/uppercase/lowercase characters in the file.

def fn():
    file1 = open("./myfile.txt","r")
    vowels = 0
    consonants = 0
    uppercase = 0
    lowercase = 0
    lst = ["a","e","i","o","u"]
    str1 = file1.read()

    for i in str1:
        if (i>"a" and i<="z"):
            lowercase += 1
        elif (i>"A" and i<="Z"):
            uppercase += 1
    for j in str1:
        j = j.lower()
        if (j in lst):
            vowels += 1
        else:
            if j.isalpha():
                consonants += 1
    print("Vowels: ",vowels)
    print("Consonants: ",consonants)
    print("Uppercase: ",uppercase)
    print("Lowercase: ",lowercase)

if __name__ == "__main__":
    fn()
