# Write a program for a simple login system.
# The program asks the user for:
# username
# password

# The correct credentials are:
# Username: admin
# Password: python123

# Rules:
# If both username and password are correct → print Login successful
# If username is correct but password is wrong → print Incorrect password
# If username is wrong → print Unknown username

# Defining the correct credentials
username = "admin"
password = "python123"

# Asking the credentials from the user and returning messages

username_input = input("User Name: ")
if username_input != username:
    print("Unknown Username")
else:
    password_input = input("Password: ")
    if password_input == password:
        print("Login Successful!!")
    else:
        print("Incorrect Password")
