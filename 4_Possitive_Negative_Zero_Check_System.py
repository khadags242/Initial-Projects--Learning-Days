# Given a list of integers, classify each number as positive, negative, or zero using if-else conditions

# Thinking hat here
# Thought this could be easily handled by using only if-else, trying to solve it using List as well; so
# Lets take in a few inputs from the user to check and store it in a list
# Based on the inputs received, lets then try to tell back the user if the numbers entered are possitive, negative or zero

# Checking with the user on the number of inputs he would like to check on

number_input = int(
    input(
        "Please let me know how many inputs would you like the program check for you: "
    )
)

# creating an empty list to store the numbers from the user
numbers = []

# Seeking inputs from the user
for i in range(1, number_input + 1):
    number = int(
        input(f"Please enter the number {i} that you would like me check on: ")
    )
    numbers.append(number)

# Inserting a Blank line between the input & output
print("\n")

# Initiating a counter for the output
counter = 1

# Assessing inputs from the user if they are ngative, possitive or a zero number
for number in numbers:
    if number < 0:
        print(f"The input {counter} i.e. {number} is a Negative Number")
    elif number > 0:
        print(f"The input {counter} i.e. {number} is a Possitive Number")
    else:
        print(
            f"The input {counter} i.e. {number} is a Zero Number and will neither be a negative or possitive number"
        )
    counter += 1

print("\n")
