# Continuously ask the user to enter numbers.
# Keep adding them together.
# Stop when the user enters 0.
# Display the final sum.

user_input = int(input("Please enter a number: "))
new = 0

while user_input != 0:
    new = user_input + new
    user_input = int(input("Please enter another number: "))

print(f"The final sum is {new}")
