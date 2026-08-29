# Restaurant Bill Calculator
# You are writing a program for a restaurant.
# The restaurant gives discounts based on the total bill:
# Bill amount	Discount
# Below ₹500	No discount
# ₹500–₹999	5%
# ₹1,000–₹1,999	10%
# ₹2,000–₹4,999	15%
# ₹5,000 and above	20%

# Your program should:

# Ask the user to enter their total bill.
# Determine the applicable discount.
# Calculate the discount amount.
# Calculate the final amount to pay.
# Print the discount and final amount.

# Asking the user to enter their total bill amount
bill_amount = float(input("Please let me know your Total Bill Amount: "))

# Determining the applicable discount
if bill_amount < 500:
    discount = 0
elif bill_amount <= 999:
    discount = 5 / 100
elif bill_amount <= 1999:
    discount = 10 / 100
elif bill_amount <= 4999:
    discount = 15 / 100
else:
    discount = 20 / 100

# Calculate the discount amount
discount_amount = round(bill_amount * discount,2)
# Calculate the final amount to pay.
final_amount = bill_amount - discount_amount

# Print the discount and final amount.
print(f"Total Discount:{discount_amount:,} i.e. {discount * 100}%")
print(f"Final amount to paid, post discount: {final_amount:,}")
