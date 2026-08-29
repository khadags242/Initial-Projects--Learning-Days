# Student Result & Grade Eligibility
# Write a program that asks a student for:
# Their marks (0–100)
# Whether they have submitted their project (yes or no)

# The rules are:
# Marks	Project	Result
# 90–100	yes	Excellent — Grade A
# 75–89	yes	Very Good — Grade B
# 60–74	yes	Good — Grade C
# 40–59	yes	Pass — Grade D
# Below 40	yes	Fail
# Any marks	no	Fail — Project not submitted

# Your program should
# Ask for the marks.
# Ask whether the project was submitted.
# Determine the result.
# Print the appropriate message.

# Ask for the marks
marks = float(input("Marks Received: "))

# Ask whether the project was submitted.
project_submission = input("Project Submitted [Yes/No]: ")

if project_submission == "No":
    print("Fail- Project Not Submitted!!")
elif marks < 40:
    print("Fail: Marks below Pass Marks")
elif marks <= 59:
    print("Pass- Grade D")
elif marks <= 74:
    print("Good - Grade C")
elif marks <= 89:
    print("Very Good- Grade B")
elif marks <= 100:
    print("Excellent- Grade A")
else:
    print("Invalid marks input")
