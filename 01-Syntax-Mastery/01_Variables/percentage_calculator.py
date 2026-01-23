'''
Percentage Calculator

Calculates percentage from favorable outcomes
out of total outcomes using basic arithmetic
'''

x = int(input("Enter number of favorable outcomes: "))
y = int(input("Enter total number of outcomes: "))

percentage = (x / y) * 100

print(f'Percentage: {percentage:.2f}%')