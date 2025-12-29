'''
Safe Input Validator
'''

# Collect user inputs and perform validation
try:

    # Collect user inputs
    age = int(input("Enter your age: "))
    height = float(input("Enter your height in meters: "))
    marks = int(input("Enter your marks (0-100): "))

    # Validate inputs
    if age <= 0:
        print("Age cannot be negative or zero")
    elif height <= 0:
        print("Height must be a positive number")
    elif marks < 0 or marks > 100:
        print("Marks must be between 0 and 100")
    else:

        # All inputs are valid, print them
        print(f'Age: {age}')
        print(f'Height: {height} meters')
        print(f'Marks: {marks}')

        # Determine pass/fail based on marks
        if marks >= 40:
            print("Pass")
        else:
            print("Fail")

# Handle non-numeric or invalid input errors
except ValueError:
    print("Invalid input! Please enter numeric values only")