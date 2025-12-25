'''
Electricity Bill Estimator
'''

# Read the number of electricity units consumed from the user
units = float(input('Enter the number of electricity units consumed:'))

# Calculate cost based on consumption slabs
if units <= 100:
    cost = units * 2.0
elif units <= 300:
    cost = units * 3.0
else:
    cost = units * 5.0

# Display the total electricity bill
print(f'Total Electricity Bill is: {cost}rs')