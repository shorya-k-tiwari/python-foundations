# Grading System

marks = int(input("Enter your marks (0–100): "))
attendance = float(input("Enter your attendance percentage (0–100): "))
if marks >= 90 and attendance >= 75:
    print("Grade: A (Excellent)")
elif marks >= 75 and attendance >= 75:
    print("Grade: B (Good)")
elif marks >= 60 and attendance >= 75:
    print("Grade: C (Average)")
else:
    print("Grade: F (Fail)")
