"""
Grading System Script

This program evaluates a student's academic performance based on
their marks and attendance percentage

Rules enforced:
- Marks must be between 0 and 100
- Attendance must be between 0 and 100
- Minimum attendance required to pass is 75%
- Grades are assigned using conditional (if-elif-else) logic only

Grades:
- A : Marks >= 90
- B : Marks >= 75
- C : Marks >= 60
- F : Marks < 60 or attendance < 75
"""

marks = int(input("Enter your marks (0-100): "))
attendance = float(input("Enter your attendance percentage (0-100): "))

if marks < 0 or marks > 100 or attendance < 0 or attendance > 100:
    print("Invalid input")
elif attendance < 75:
    print("Grade: F (Fail due to low attendance)")
elif marks >= 90:
    print("Grade: A (Excellent)")
elif marks >= 75:
    print("Grade: B (Good)")
elif marks >= 60:
    print("Grade: C (Average)")
else:
    print("Grade: F (Fail)")