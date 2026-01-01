'''
Palindrome Number Checker
'''

#
n = int(input('Enter a Number: '))

#
m = 0

#
if 0 <= n <= 9:
    answer = 'Palindrome'
elif n>9:
    
    #
    original = n 
    
    #
    while n!=0:
        digit = n%10
        m = m*10 + digit
        n = n//10

    # 
    if m == original:
        answer = 'Palindrome'
        print(f'{original} ---> {answer}')
        exit()
    else:
        answer = 'Not a Palindrome'
        print(f'{original} ---> {answer}')
        exit()
elif n<0:
    answer = 'Not a Palindrome'
else:
    print('Please enter a Numeric Value!')
    exit()

#
print(f'{n} ---> {answer}')