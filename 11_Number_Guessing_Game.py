# The computer chooses a number.
# Keep asking the user to guess until they get it right.
# Tell them whether their guess is too high or too low.
# Track the number of attempts.

# import the python's ability to think of a random number
import random

# define the range in which the numbers will be thought by the program
a = int(input("Please enter the starting range: "))
b = int(input("Please enter the ending range: "))

# generate a random number as the base number by the computer. This is the number the user needs to guess
num = random.randint(a, b)

# ask for the user's input and start counting
user_input = int(input(f"Please guess the computer's number from {a} to {b}: "))
count = 1

# start checking number if this is the correct number
while user_input != num:
    # check if the user input is outside the range & below the starting point of the range
    if user_input < a:
        print("You have entered a number below the allowed range.")
    # check if the user input is outside the range & above the ending point of the range
    elif user_input > b:
        print("You have entered a number above the allowed range.")
    # check if the user input is within the range but smaller than the guessed number
    elif user_input < num:
        print("Your guess is too low!")
    # check if the user input is within the range but higher that the guessed number
    else:
        print("Your guess is too high!")

    # Ask the user for his input again
    print("Please try again!")
    user_input = int(input(f"Please guess the computer's number from {a} to {b}: "))
    count = count + 1

# print the final messgae & display the count of attempts taken
print(f"You guessed the correct number in {count} attempts!")
