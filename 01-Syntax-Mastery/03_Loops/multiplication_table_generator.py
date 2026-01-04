'''
Multiplication Table Generator

A multiplication table is a mathematical list or grid 
that shows the results of multiplying one number by a set of others
'''

# Take the number whose table is to be generated
number = int(input('Enter a Number: '))

# Take how many multiples the user wants
count = int(input('Enter the number of multiples to generate: '))

# Validate the count input
if count < 0:
    print('Count cannot be negative!')
    exit()

# Display table header
print('\n', f'|=== Multiplication Table ===|')

# Generate multiplication table using for loop
for i in range(1, count + 1):
    print(f'{number} x {i} = {number * i}')