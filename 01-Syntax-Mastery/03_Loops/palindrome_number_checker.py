"""
Palindrome Number Checker

Checks whether an integer reads the same forwards and backwards
"""

n = int(input("Enter a number: "))
original = n
reversed_num = 0

if n < 0:
    result = "Not a Palindrome"
elif n == 0:
    result = "Palindrome"
else:
    while n > 0:
        reversed_num = reversed_num * 10 + n % 10
        n //= 10

    result = "Palindrome" if reversed_num == original else "Not a Palindrome"

print(f"{original} ---> {result}")