'''
Eligibility Decision Engine
'''

# Collect user inputs
age = int(input("Enter your age: "))
math = int(input("Enter your Math score (0-100): "))
physics = int(input("Enter your Physics score (0-100): "))
experience = int(input("Enter your years of coding experience: "))
discipline = int(input("Enter your discipline score (1-10): "))

# Determine eligibility status
if age<16 or math<60 or physics<60:
    status = 'Rejected (Core requirements not met)'
elif math>=85 and physics>=85 and experience>=2 and discipline>=8:
    status = 'Eligible'
elif math>=70 and physics>=70:
    status = 'Waitlisted'
else:
    status = 'Rejected (Does not meet eligibility criteria)'

# Output the eligibility status
print(f'Status: {status}')