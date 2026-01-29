'''
Sum of Digits Calculator

Calculates the sum of all digits of an integer using iteration.
'''

num = int(input("Enter an integer: "))
n = abs(num)
total = 0

while n > 0:
    total += n % 10
    n //= 10

print(f"Sum of Digits: {total}")