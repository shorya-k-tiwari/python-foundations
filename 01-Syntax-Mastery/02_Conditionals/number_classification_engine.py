'''
Number Classification Engine
'''

# Input from user
n=int(input("Enter a number: "))

# Initializing output header
output= 'Output'

# Checking sign
if n>0:
    sign = "Positive"
elif n<0:
    sign = "Negative"
else:
    sign = "Neither Positive nor Negative. It is Zero"

# Checking parity
if n%2==0:
    parity = "Even"
else:
    parity = "Odd"

# Checking divisibility by 3 and 5
if n%3==0 and n%5==0:
    divisibility = "Multiple of both 3 and 5"
elif n%3==0 and n%5!=0:
    divisibility = "Multiple of 3 only"
elif n%5==0 and n%3!=0:
    divisibility = "Multiple of 5 only"
else:
    divisibility = "Not a multiple of both 3 or 5"

# Output results
print(f'Input Number: {n}')
print()
print(f'{output:=^36}')
print(f'Sign: {sign}')
print(f'Parity: {parity}')
print(f'Divisibility: {divisibility}')