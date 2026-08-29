# Build a simple ATM withdrawal program.

# The ATM starts with:
# Account balance = ₹10,000

# Ask the user:
# How much money would you like to withdraw?
# Then apply these rules:
# 1- If the withdrawal amount is less than or equal to ₹0 → print Invalid withdrawal amount
# 2- If the withdrawal amount is greater than the account balance → print Insufficient balance
# 3- If the withdrawal amount is not a multiple of ₹100 → print Please enter an amount in multiples of ₹100
# Otherwise:
# 1- Deduct the withdrawal amount from the balance.
# 2- Print the amount withdrawn.
# 3- Print the remaining balance.

# Defining the account balance to start with
balance = 10000

# Asking the user for the withdrawal amount
amount_withdraw = int(input("Amount to be withdrawan: "))

# Checking the rules & pronting messages

if amount_withdraw <= 0:
    print("Invalid withdrawal amount!")
elif amount_withdraw > balance:
    print("Insufficient Balance!!")
elif amount_withdraw % 100 != 0:
    print("Please enter an amount in multiple of 100!!")
else:
    balance_new = balance - amount_withdraw
    print(f"Amount withdrawn: {amount_withdraw:,}")
    print(f"Balance remaining: {balance_new:,}")
