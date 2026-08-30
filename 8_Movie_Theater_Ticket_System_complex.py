# The program should ask the customer for:
# 1. Age
# 2. Day of the week
# 3. Number of tickets
# 4. Whether they have a student ID (yes / no)
# Base ticket prices
# 1. Customer	Base price
# 2. Child — under 13	₹100
# 3. Adult — 13–59	₹200
# 4. Senior — 60+	₹150
# Day-based discount
# The theater has a special discount on Wednesday:
# 1. Wednesday → 20% discount
# 2. Every other day → no day discount
# Student discount
# Students get an additional 10% discount, but only if:
# 1. They are between 13 and 25 years old, and
# 2. They have a student ID.
# So:
# Age 20 + student ID = student discount
# Age 20 + no student ID = no student discount
# Age 30 + student ID = no student discount
# Group discount
# 1. If the customer buys 5 or more tickets, they receive an additional 5% group discount.

age = int(input("Please enter the age: "))
day = input("Please enter the day of the week for the movie (M/T/W/T/F/S/S): ").lower()
number_ticket = int(input("Number of tickets: "))
student_id = input("With Student ID (Y/N): ").lower()

# defining the ticket prices
if age < 0:
    print("Invalid age!")
else:
    if age < 13:
        price = 100
    elif age <= 59:
        price = 200
    else:
        price = 150

    # defining the discount slabs
    if day == "w":
        discount1 = 20 / 100
    else:
        discount1 = 0

    if number_ticket >= 5:
        discount2 = 5 / 100
    else:
        discount2 = 0

    if 13 <= age <= 25:
        if student_id == "y":
            discount3 = 10 / 100
        else:
            discount3 = 0
    else:
        discount3 = 0

    ticket_price = price * number_ticket
    ticket_price1 = ticket_price - (ticket_price * discount1)
    ticket_price2 = ticket_price1 - (ticket_price1 * discount3)
    ticket_price3 = round(ticket_price2 - (ticket_price2 * discount2), 2)

    print(f"Final Ticket Amount: {ticket_price3:,}")
