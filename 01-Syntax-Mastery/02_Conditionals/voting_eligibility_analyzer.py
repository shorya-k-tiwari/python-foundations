'''
Voting Eligibility Analyzer
'''

# Get user input for age
age = int(input("Enter your age: "))

# Determine voting eligibility based on age
if age >= 18:
    print("You are eligible to vote")
elif age > 0:
    year = 18 - age
    print(f"You are not eligible. You can vote after {year} year(s)")
else:
    print("Invalid age entered")