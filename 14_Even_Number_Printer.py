# Ask the user for a number.
# Print all even numbers from 0 up to that number.

num = int(input("Please enter a number: "))
start = 0
# start=start+2
count = 1

while start <= num:
    # start = start + 2
    print(f"Even Number{count}: {start}")
    start = start + 2
    count = count + 1

# print("Thank You")
