# You're writing a program to calculate an electricity bill.

# The electricity company charges according to units consumed:
# Units consumed	Rate
# 0–100	    ₹5 per unit
# 101–200	₹7 per unit
# 201–300	₹10 per unit
# Above 300	₹15 per unit
# Your program should
# 1- Ask the user how many electricity units they consumed.
# 2- Determine the applicable rate.
# 3- Calculate the total bill.
# 4- Print the units consumed, rate per unit, and total bill.

units_consumed = float(input("Units Consumed: "))

if units_consumed < 0:
    print("Invalid Units Consumed!!")
else:
    if units_consumed <= 100:
        rate_per_unit = 5
    elif units_consumed <= 200:
        rate_per_unit = 7
    elif units_consumed <= 300:
        rate_per_unit = 10
    else:
        rate_per_unit = 15

    total_bill = round(units_consumed * rate_per_unit, 2)
    print(
        f"Units consumed:{units_consumed} \nRate per unit:{rate_per_unit} \nTotal Bill: {total_bill:,}"
    )
