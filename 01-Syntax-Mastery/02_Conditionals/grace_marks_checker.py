"""
Grace Marks Checker

Evaluates pass/fail status by applying a fixed grace rule to borderline marks
"""

marks = float(input("Enter your marks: "))

if marks < 0:
    print("Invalid input. Marks cannot be negative")
    status = None

elif marks <= 33:
    grace = marks + 5

    if grace > 33:
        status = "Pass"
        note = "Work Hard"
    else:
        status = "Fail"
        note = "Needs Improvement"

else:
    grace = marks
    status = "Pass"
    note = "Good Job!"

if status is not None:
    print(f"Actual Marks : {marks}")
    print(f"Final Marks  : {grace}")
    print(f"Status       : {status}")
    print(f"Note         : {note}")