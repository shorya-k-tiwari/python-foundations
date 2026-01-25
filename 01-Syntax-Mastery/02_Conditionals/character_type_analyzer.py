'''
Character Type Analyzer

Classifies a single character as uppercase, lowercase, digit, or special
'''

char = input("Enter a single character: ")

if len(char) != 1:
    result = "Please enter exactly one character"

elif 'A' <= char <= 'Z':
    result = "Uppercase Character"

elif 'a' <= char <= 'z':
    result = "Lowercase Character"

elif '0' <= char <= '9':
    result = "Digit Character"

else:
    result = "Special Character"

print(f"Result: {result}")