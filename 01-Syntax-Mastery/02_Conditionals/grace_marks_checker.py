'''
Grace Marks Checker
'''

# Take marks input from the user
marks = float(input('Enter your marks: '))

# Validate marks input
if marks < 0:
    print('Marks cannot be negative!')
    exit()

# Apply grace marks if marks are less than or equal to 33
elif marks <= 33:
    grace = marks + 5

    # Check pass/fail after grace marks
    if grace > 33:
        status = 'Pass'
        note = 'Work Hard'
    else:
        status = 'Fail'
        note = 'Needs Improvement'

# If marks are already above passing marks
else:
    grace = marks
    status = 'Pass'
    note = 'Good Job!'        

# Display final result
print(f'Actual marks: {marks}')
print(f'Grace marks: {grace}')
print(f'Status: {status}')
print(f'Note: {note}')