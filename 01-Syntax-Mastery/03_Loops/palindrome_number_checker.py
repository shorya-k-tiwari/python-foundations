'''
Palindrome Number Checker
'''

# Take integer input from the user
n = int(input('Enter a Number: '))

# Store the original number for comparison
original = n

# Variable to store the reversed number
m = 0

# Handling -ve numbers
if n < 0:
    answer = 'Not a Palindrome'

# Zero is a palindrome
elif n == 0:
    answer = 'Palindrome'

# Reverse the number and compare
else:
    temp = n
    while temp != 0:
        digit = temp % 10
        m = m * 10 + digit
        temp //= 10
    
    # Check if reversed number matches the original
    answer = 'Palindrome' if m == original else 'Not a Palindrome'

# Display the result
print(f'{original} ---> {answer}')