# Problem
# Build a simple banking transaction program.
#   Starting balance: ₹25,000
#   Ask the user:
#   1- Transaction type: deposit or withdraw
#   2- Amount

# Rules:
#   1- Deposit
#       a. Amount ≤ ₹0 → Invalid deposit amount
#       b. Otherwise → add the amount to the balance
#   2- Withdrawal
#       a. Amount ≤ ₹0 → Invalid withdrawal amount
#       b. Amount greater than balance → Insufficient balance
#       c. Amount is not a multiple of ₹100 → Withdrawal must be in multiples of ₹100
#       d. Otherwise → deduct the amount
#   3- Final output
#   For a successful transaction, display:
#   a- Transaction successful
#   b- Transaction amount: ₹____
#   c- Remaining balance: ₹____

# Setting the strating account balance
starting_balance = 25000

# Seeking input on the type of transaction
transaction_type = input("Transaction Type (W for Withdrawal, D for Deposti): ").lower()
transaction_amount = float(input("Transaction amount: "))

if transaction_amount <= 0:
    print("Invalid amount!")

else:
    if transaction_type == "d":
        new_amount = starting_balance + transaction_amount
        print("Transaction Successful")
        print(f"Transaction amount: {transaction_amount:,}")
        print(f"Remaining Balance {new_amount: ,}")
    elif transaction_type == "w":
        if transaction_amount % 100 != 0:
            print("Invalid amount, amount needs to be in multiple of 100")
        else:
            if transaction_amount > starting_balance:
                print("Insufficient Balance")
            else:
                new_amount = starting_balance - transaction_amount
                print("Transaction Successful")
                print(f"Transaction amount: {transaction_amount:,}")
                print(f"Remaining Balance {new_amount: ,}")
