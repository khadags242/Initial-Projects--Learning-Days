# Filter and Count Specific Words in a List- Given a list of strings, count how many times certain words (e.g., "apple", "banana") appear and print the result.

# Thinking hat on
# Check element by element how many times the element is appearing in a list

# Defining the list
strings = []

# Inserting elements in the list to check
strings_addition = input("Please enter an element in the list: ")
strings.append(strings_addition)

# Checking with user if they want to add in more elesments
check_more = input(
    "Would you like to input more elements in the list (Y for Yes/ N for No): "
)

while check_more.lower() == "y":
    strings_addition = input("Please enter an element in the list: ")
    strings.append(strings_addition)
    check_more = input(
        "Would you like to input more elements in the list (Y for Yes/ N for No): "
    )

for string in set(strings):
    count = strings.count(string)
    if count > 1:
        print(f"\n{string} is a repetative string. This is appearing {count} times")
    else:
        print(f"\n{string} is a non repetative string!")
