''' 
Digit to Word Converter

Digit to Word Converter is mapping numbers to spelled-out 
English words via place-value grouping and lookup tables
'''

# Get a digit input from the user
n = int(input('Enter a Digit (0-9): '))

# Convert digit to its word representation
if n == 0:
    digit = 'Zero'
elif n == 1:
    digit = 'One'
elif n == 2:
    digit = 'Two'
elif n == 3:
    digit = 'Three'
elif n == 4:
    digit = 'Four'
elif n == 5:
    digit = 'Five'
elif n == 6:
    digit = 'Six'
elif n == 7:
    digit = 'Seven'
elif n == 8:
    digit = 'Eight'
elif n == 9:
    digit = 'Nine'
else: 
    print('Invalid Digit!')
    exit()

# Display the result
print(f'{digit}')