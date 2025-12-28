# Grade Assignment System- Create a program where the user inputs a list of student scores. Based on each score, assign a grade:
# A: 90-100
# B: 80-89
# C: 70-79
# D: 60-69
# F: 0-59

# Thingking hat on
# Check for the number of students this entry needs to go in
# Assign a set of marks against each of these students i.e. student1, student 2etc.
# Check the marks against the scale provided
# Assign grades based on these marks
# Display output

# Checking for the number of students the marks need to be fed in
students_numbers = int(
    input(
        "Please enter the number of students you would like to enter into our grading mechanism: "
    )
)

# Defining the list caleed scores to strore the score inputs
scores = []

# Seeking inputs on scores & feeding them in the list called Scores to store them
for i in range(1, students_numbers + 1):
    score = int(input(f"Please enter the score {i}: "))
    scores.append(score)

# Printing a blank line betwee the input & grading outputs
print("\n")
counter = 1

# Assessing Marks & their subsequent output grades
for score in scores:
    if 90 <= score <= 100:
        print(f"For Score {counter} i.e. {score}: your grade is A")
    elif 80 <= score <= 89:
        print(f"For Score {counter} i.e. {score}: your grade is B")
    elif 70 <= score <= 79:
        print(f"For Score {counter} i.e. {score}: your grade is C")
    elif 60 <= score <= 69:
        print(f"For Score {counter} i.e. {score}: your grade is D")
    elif 0 <= score <= 59:
        print(f"For Score {counter} i.e. {score}: your grade is F")
    counter += 1

print("\n")
