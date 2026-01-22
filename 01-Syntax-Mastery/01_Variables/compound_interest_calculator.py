'''
Compound Interest Calculator

Calculates compound interest using principal, rate, time, and compounding frequency
'''

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual interest rate (in %): "))
n = int(input("Enter the number of times interest is compounded per year: "))
t = int(input("Enter the number of years: "))

ci = principal * (1 + rate / (100 * n)) ** (n * t) - principal

print(f"Compound interest after {t} years: {ci:.2f}")