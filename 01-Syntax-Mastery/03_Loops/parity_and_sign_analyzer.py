'''
Parity and Sign Analyzer
'''

# Initialize counters for different classifications
odd = even = negative = positive = zero = 0

# Ask the user how many numbers they want to enter
count = int(input('Enter how many numbers will you enter? '))

# Validate count (cannot be negative)
if count < 0:
    print('Count cannot be zero!')

# Loop to accept numbers one by one
for i in range(count):

    # Read a number from the user
    n = int(input('Enter a number: '))

    # Check the sign of the number
    if n > 0:
        positive += 1
    elif n == 0:
        zero += 1
    elif n < 0:
        negative += 1
    
    # Check the parity of the number
    if n % 2 == 0:
        even += 1
    elif n % 2 != 0:
        odd += 1

# Display the final counts
print('\n', '|=== Summary ===|')
print(f'Positive Numbers: {positive}')
print(f'Negative Number: {negative}')
print(f'Zeroes: {zero}')
print(f'Odd Numbers: {odd}')
print(f'Even Numbers: {even}')