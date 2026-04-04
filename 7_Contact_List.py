# Create a contact book where users can add, view, and search for contacts by name or number.
# The features to include
# Add new contacts with a name and phone number.
# View all saved contacts.
# Search for a contact by name.

# Createing the list for names & contacts
names = []
contacts = []

count = 1

# Building the directory
contact_name = input(f"Please input the name of the person {count}: ").strip().title()
names.append(contact_name)
contact_number = input(
    f"Please input the contact number of the person {count}: "
).strip()
contacts.append(contact_number)

check_to_add_more = input(
    "Please let me know if you would like to add more contacts (Y for Yes/N for No): "
)

while check_to_add_more.lower() == "y":
    count += 1
    contact_name = (
        input(f"Please input the name of the person {count}: ").strip().title()
    )
    names.append(contact_name)
    contact_number = input(
        f"Please input the contact number of the person {count}: "
    ).strip()
    contacts.append(contact_number)
    check_to_add_more = input(
        "Please let me know if you would like to add more contacts (Y for Yes/N for No): "
    )

print(names, contacts)

# Checking for next step
next_step = input(
    "\nWhat would you like to do next, R to retrieve details or S to retrieve specific details: "
)

# initiating new count
count2 = 0

print()

# Proceeding forward if the choice made was to retrieve all contact list
if next_step.lower() == "r":
    while len(names) > count2:
        print(f"Contact {count2 + 1}       {names[count2]}         {contacts[count2]}")
        count2 += 1

# Proceeding forward if the choice made was to retrieve all contact list
elif next_step.lower() == "s":
    find_parameter = input(
        "Would you like to find a specific information by name or number: "
    )
    if find_parameter.lower() == "name":
        find_name = input("Please input the name to be found: ").strip().title()

        if find_name in names:
            index = names.index(find_name)
            print(f"Contact {index + 1}       {find_name}         {contacts[index]}")
        else:
            print("Contact not found.")
