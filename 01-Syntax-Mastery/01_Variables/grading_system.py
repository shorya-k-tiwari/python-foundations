'''
Grading System Based on Marks and Attendance
'''

# Read student's marks (0–100) and attendance percentage (0–100) from the user
marks = int(input("Enter your marks (0–100): "))
attendance = float(input("Enter your attendance percentage (0–100): "))

# Initialize grade variable
grade = ""

# Determine grade based on marks and minimum attendance requirement (75%)
if marks >= 90 and attendance >= 75:
    grade = "Grade: A (Excellent)"
elif marks >= 75 and attendance >= 75:
    grade = "Grade: B (Good)"
elif marks >= 60 and attendance >= 75:
    grade = "Grade: C (Average)"
else:
    grade = "Grade: F (Fail)"

# Display the determined grade
print(grade)