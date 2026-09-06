# Ask the user for a number and determine:
# Whether it is even or odd.
# Whether it is positive, negative, or zero.
# Keep asking for numbers until the user chooses to stop.

number=(input("Please enter a number (q to quit): "))

while number.lower()!="q":

    while number=="":
        print("You havent input anything yet!!")
        number=(input("Please enter a number (q to quit): "))
        
    if number.lower()=="q":
        print("bye bye")
    else:
        number=int(number)
        number_checker=number%2
        if number==0:
            print("Number is 0 and hence even")
        elif number<0:
            if number_checker!=0:
                print("Number is -ve & odd")
            else:
                print("Number -ve & even")
        else:
            if number_checker!=0:
                print("Number is +ve & odd")
            else:
                print("Number is +ver & even")
    
    number=input("Another number to try (q to quit): ")

print("bye bye")