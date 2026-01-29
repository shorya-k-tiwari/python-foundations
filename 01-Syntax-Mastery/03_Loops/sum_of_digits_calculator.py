'''
Sum of Digits Calculator
'''

num = int(input('Enter an Integer:'))  
n = abs(num)         
sum = 0

while n > 0:
    sum += n % 10   
    n //= 10              

print(f'Sum of Digits: {sum}')