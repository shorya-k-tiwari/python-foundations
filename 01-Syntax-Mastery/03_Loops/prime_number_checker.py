"""
Prime Number Checker

Determines whether a given integer is prime.
"""

from math import sqrt

n = int(input("Enter a positive integer: "))

if n <= 0:
    print("Invalid input! Prime numbers are greater than 1")
    exit()
elif n == 1:
    print("1 is neither prime nor composite")
    exit()

is_prime = True

for i in range(2, int(sqrt(n)) + 1):
    if n % i == 0:
        is_prime = False
        break

if is_prime:
    print(f"{n} is a Prime Number")
else:
    print(f"{n} is a Composite Number")