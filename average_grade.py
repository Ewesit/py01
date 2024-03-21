# Initialize a variable to store the sum of grades
total_grades = 0

# Iterate over each student
for i in range(1, 11):
    # Input the grade for each student
    grade = float(input(f"Enter the grade for student {i}: "))
    
    # Add the grade to the total
    total_grades += grade

# Calculate the average grade
average_grade = total_grades / 10

# Print the average grade
print(f"The average grade for the class is: {average_grade}")
