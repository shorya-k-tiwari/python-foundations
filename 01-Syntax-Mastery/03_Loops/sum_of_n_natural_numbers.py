'''
Sum of n Natural Numbers
'''

n = int(input("Enter a positive integer: "))

if n < 0:
    print('Please enter a positive integer')
else:
    sum = 0
    for i in range(1, 1 + n):
        sum += i