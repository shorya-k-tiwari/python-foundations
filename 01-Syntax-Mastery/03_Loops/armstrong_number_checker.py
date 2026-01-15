"""
Armstrong Number Checker

Checks whether a number equals the sum of its digits
raised to the power of the number of digits
"""

n = int(input("Enter a number: "))

if n < 0:
    result = "Not an Armstrong Number"
elif n == 0:
    result = "Armstrong Number"
else:
    digits = 0
    temp = n
    armstrong_sum = 0

    while temp > 0:
        digits += 1
        temp //= 10

    temp = n
    while temp > 0:
        armstrong_sum += (temp % 10) ** digits
        temp //= 10

    result = "Armstrong Number" if armstrong_sum == n else "Not an Armstrong Number"

print(f"{n} ---> {result}")