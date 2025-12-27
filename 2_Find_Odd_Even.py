# Write a program to fine Even and Odd Numbers in a List
# Given a list of numbers, categorize them into even and odd numbers and print them separately.

# thinking mode on
# first define a list
# take inputs from the user for the start of the list and the end of the list
# use range function to define the list based on the user parameter
# start running check if it is even or odd- simple step, if its 0 or divisible by 2, then even else odd
# print number by number the result

# Starting to write the program

# defining the list name
# numbers=[]

# ask for the range start and end paramters from the user
range_start = int(input("Please input the starting point of the range to be checked: "))
range_end = int(input("Please input the ending point of the range to be checked: "))

# Defining the list basis the parameters entered
numbers = list(range(range_start, range_end))
#print(numbers)

# checking & printing the results if they arodd or even
for number in numbers:
    if number%2 != 0:
        print(f"\n{number} is Odd")

    else:
        print(f"{number} is Even")
