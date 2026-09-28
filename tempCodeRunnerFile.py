# The computer chooses a number.
# Keep asking the user to guess until they get it right.
# Tell them whether their guess is too high or too low.
# Track the number of attempts.

# enabling the program to guess a random number between 1 to 10
import random
num=random.randint(1,10)
print(num)

user_input=int(input(("Please guess the computer guessed number from 1 to 10")))
count=0

while num!=user_input:
    print("You have not guessed the correct number!!")
    user_input=("Please re- guess the computer guessed number from 1 to 10")
    count=count+1
    
print(f"COngratulations! you guessed the correct number in {count} attempt")
    
    

