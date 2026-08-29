# problem write up
# The cinema charges different ticket prices depending on the customer's age:
# Age	Ticket Price
# Under 5	Free
# 5–12	₹100
# 13–17	₹150
# 18–59	₹250
# 60 and above	₹180
# Your program should:
# i. Ask the user for their age.
# ii. Determine the correct ticket price.
# iii. Print the price.

# Ask input from the user for his age
age = int(input("Please enter your age: "))

# test the age based on parameters and then suggest the output

if age <= 0:
    print(f"{age} is invalid")
elif age < 5:
    print(f"Since you are {age} yrs. old. you get to see the cinema for free")
elif age <= 12:
    print(f"Since you are {age} yrs. old; your cinema ticket will be Rs. 100")
elif age <= 17:
    print(f"Since you are {age} yrs. old; your cinema ticket will be Rs. 150")
elif age <= 59:
    print(f"Since you are {age} yrs. old; your cinema ticket will be Rs. 250")
else:
    print(f"Since you are {age} yrs. old; your cinema ticket will be Rs. 180")
