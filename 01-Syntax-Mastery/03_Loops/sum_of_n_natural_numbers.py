"""
Sum of n Natural Numbers

Computes the sum of the first n natural numbers using iteration.
"""

n = int(input("Enter a positive integer: "))

if n <= 0:
    result = "Invalid input: n must be greater than 0"
else:
    total = 0
    for i in range(1, n + 1):
        total += i
    result = f"The sum of the first {n} natural numbers is {total}"

print(result)