# Write a python program to count Vowels and Consonants in a String.

def count(n):
    arr = ['a','e','i','o','u']
    vowels = 0
    consonent = 0
    n = n.lower()
    for i in n:
        if i in arr:
            vowels = vowels + 1
        else:
            consonent = consonent + 1
    print(f'Number of vowels = {vowels} and number of consonent = {consonent}')

if __name__ == '__main__':
    n = str(input("Enter string ="))
    count(n)