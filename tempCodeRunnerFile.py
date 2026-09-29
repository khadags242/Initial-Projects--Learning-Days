# Ask the user for a number.
# Generate its multiplication table.
# Ask if they want another table.
# Continue until they choose to stop.

num_for_table = int(
    input("Please enter the number for which multiplication table needs to be built: ")
)
num_multiplier = int(
    input(
        "Please enter the multiplier to which you would like to build the table for: "
    )
)

counter = 0

while counter <= num_multiplier:
    output = num_for_table * counter
    print(f"{num_for_table}*{counter}= {output}")
    counter = counter + 1

new_request = input("Would you like to print another table (y/n): ")

while new_request == "y":
    num_for_table = int(
        input(
            "Please enter the number for which multiplication table needs to be built: "
        )
    )
    num_multiplier = int(
        input(
            "Please enter the multiplier to which you would like to build the table for: "
        )
    )

    counter = 0

    while counter <= num_multiplier:
        output = num_for_table * counter
        print(f"{num_for_table}*{counter}= {output}")
        counter = counter + 1
    new_request = input("Would you like to print another table (y/n): ")

print("Thank you")
