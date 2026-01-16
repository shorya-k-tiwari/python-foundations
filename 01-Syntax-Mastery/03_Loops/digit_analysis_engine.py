"""
Digit Analysis Engine

Analyzes the digits of a positive integer to compute
their sum, product, and parity of the sum
"""

n = int(input("Enter a positive integer: "))

if n <= 0:
    print("Invalid input")
    exit()

digit_sum = 0
digit_product = 1
temp = n

while temp > 0:
    digit = temp % 10
    digit_sum += digit
    digit_product *= digit
    temp //= 10

parity = "Even" if digit_sum % 2 == 0 else "Odd"

print("Output:")
print(f"Sum of digits: {digit_sum}")
print(f"Product of digits: {digit_product}")
print(f"Parity of sum: {parity}")