'''
Digit Analysis Engine
'''

# Input: Read a positive integer from the user
n=int(input("Enter a positive integer: "))

# Initialize variables to accumulate sum and product of digits
sum = 0
product = 1

# Process each digit of the number
while n>0:
    digit = n % 10
    sum += digit
    product *= digit
    n //=10

# Determine the parity of the sum
if sum%2==0:
    parity = "Even"
else:
    parity = "Odd"

# Output the results
print('Output:-')
print(f"Sum of digits: {sum}")
print(f"Product of digits: {product}")
print(f"Parity of sum: {parity}")