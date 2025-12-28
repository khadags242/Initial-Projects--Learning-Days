# Create a list of names and ages. Classify each person as either a "child" (0-12), "teenager" (13-19), "adult" (20-64), or "senior" (65+)

# Thinking Hat on
# We need to first check the number of users for whom we are seeking the input for i.e. 4 people, 6 people etc.
# once clarified, we will then have to take the input on names, store it in a name list
# Take in the subsequent age input as well and store them in a list for age
# Perform the test, based on the conditions specified
# Print out the output by calling out name and age basis which the classification has been made

# defining the lists, names & ages
names = []
ages = []

# Seeking inputts- the first one
count_people = 1
names_list = input(
    f"Please input the name of the person {count_people} to be checked: "
)
names.append(names_list)
age_list = int(input((f"Please input the age for {names_list}: ")))
ages.append(age_list)

# Checking if there are more names to be filled in- power back to the user
check_for_more_input = input(
    "\nWould you like to enter more names (Y for Yes/N for No): "
)

# Creating the input loop till the time the user says no more
while check_for_more_input.upper() == "Y":
    count_people += 1
    names_list = input(
        f"Please input the name of the person {count_people} to be checked: "
    )
    names.append(names_list)
    age_list = int(input(f"Please input the age for {names_list}: "))
    ages.append(age_list)
    check_for_more_input = input(
        "\nWould you like to enter more names (Y for Yes/N for No): "
    )

# Creating a counter to use as index in List
count2 = 0

# Performing assessment to classify into age groups basis the age
for age in ages:
    if age >= 65:
        print(f"Since {names[count2]} is {age} yrs. old, he is therefore a Senior")
    elif 20 <= age <= 64:
        print(f"Since {names[count2]} is {age} yrs. old, he is therefore a Adult")
    elif 13 <= age <= 19:
        print(f"Since {names[count2]} is {age} yrs. old, he is therefore a Teenager")
    elif 0 <= age <= 12:
        print(f"Since {names[count2]} is {age} yrs. old, he is therefore a Child")
    else:
        print(f"Since {names[count2]} is {age} yrs. old, the entered value is invalid")
    count2 += 1

print("\n")
