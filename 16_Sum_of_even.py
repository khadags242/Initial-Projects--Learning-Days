# Ask the user for a number n.
# Calculate the sum of all even numbers from 1 to n.

num = int(input("Please input a number: "))

count = 0
start = 0

while count <= num:
    start = start + count
    count = count + 2

print(f"The sum of all even numbers upto {num} is {start}")
