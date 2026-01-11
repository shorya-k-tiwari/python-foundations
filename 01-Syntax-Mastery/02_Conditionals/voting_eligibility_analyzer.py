"""
Voting Eligibility Analyzer

Determines voting eligibility based on age
"""

age = int(input("Enter your age: "))

if age < 0:
    print("Invalid age entered")
elif age >= 18:
    print("You are eligible to vote")
else:
    years_left = 18 - age
    print(f"You are not eligible. You can vote after {years_left} year(s)")