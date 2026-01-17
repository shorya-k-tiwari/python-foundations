"""
Safe Input Validator

Validates user input and determines pass/fail status
"""

try:
    age = int(input("Enter your age: "))
    height = float(input("Enter your height in meters: "))
    marks = int(input("Enter your marks (0-100): "))

    if age <= 0:
        print("Age must be a positive number")
    elif height <= 0:
        print("Height must be a positive number")
    elif marks < 0 or marks > 100:
        print("Marks must be between 0 and 100")
    else:
        print(f"Age   : {age}")
        print(f"Height: {height} meters")
        print(f"Marks : {marks}")

        if marks >= 40:
            print("Result: Pass")
        else:
            print("Result: Fail")

except ValueError:
    print("Invalid input! Please enter numeric values only")