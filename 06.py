# Write a program to generate random numbers between 1 to 6 and check whether a user won a lottery or not.

from random import randint as ri

def create_random_number():
    n = ri(1, 6)
    return n
def guess_number(n):
    while True:
        try:
            guess = int(input("Guess a number between 1 to 6: "))
            if guess > 6 or guess < 1:
                print("Out of range. Please enter number between 1 to 6.")
            elif guess == n:
                print("You won the lottery!")
                break
            else:
                print("Try again!")
        except ValueError:
            print("Please enter a number!")
if __name__ == "__main__":
    n = create_random_number()
    guess_number(n)
