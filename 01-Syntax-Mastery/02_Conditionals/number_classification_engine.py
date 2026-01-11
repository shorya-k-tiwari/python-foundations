"""
Number Classification Engine

Determines the sign, parity, and divisibility
properties of an input integer
"""

n = int(input("Enter a number: "))

if n > 0:
    sign = "Positive"
elif n < 0:
    sign = "Negative"
else:
    sign = "Zero"

if n % 2 == 0:
    parity = "Even"
else:
    parity = "Odd"

if n % 3 == 0 and n % 5 == 0:
    divisibility = "Multiple of both 3 and 5"
elif n % 3 == 0:
    divisibility = "Multiple of 3 only"
elif n % 5 == 0:
    divisibility = "Multiple of 5 only"
else:
    divisibility = "Not a multiple of 3 or 5"

print(f"\nInput Number: {n}")
print('|=== Output ===|')
print(f"Sign        : {sign}")
print(f"Parity      : {parity}")
print(f"Divisibility: {divisibility}")