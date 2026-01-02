'''
Prime Number Checker

A prime number is a positive integer 
greater than 1 that has no positive divisors other than 1 and itself
'''

# Import necessary function 
from math import sqrt

# Take input from the user
n = int(input("Enter a positive integer: "))

# Numbers less than 1 are not prime
if n < 1:
    print("Invalid input! Prime numbers are greater than 1")
    exit()
elif n == 1:
    print(f'{n} is Neither Prime Nor Composite')
    exit()
else:
    prime = True  # Assume prime initially

    # Check divisibility
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            prime = False
            break

# Display the result
if prime:
    print(f"{n} is a Prime Number")
else:
    print(f"{n} is a Composite Number")