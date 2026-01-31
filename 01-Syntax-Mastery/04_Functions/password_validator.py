"""
Early Return Password Validator

Validates a password using guard clauses
to avoid nested conditionals

Rules:
- Length ≥ 8
- Contains at least one uppercase letter
- Contains at least one lowercase letter
- Contains at least one digit
- Contains at least one special character
"""

def password_checker(pwd):

    if len(pwd) < 8:
        return "Invalid: Password must be at least 8 characters long"

    upper = False
    lower = False
    digit = False
    special = False

    for i in pwd:
        if 'A' <= i <= 'Z':
            upper = True
        elif 'a' <= i <= 'z':
            lower = True
        elif '0' <= i <= '9':
            digit = True
        else:
            special = True

    if not upper:
        return "Invalid: Missing uppercase letter"
    if not lower:
        return "Invalid: Missing lowercase letter"
    if not digit:
        return "Invalid: Missing digit"
    if not special:
        return "Invalid: Missing special character"
    return "Password is valid"


password = input("Enter password: ")
result = password_checker(password)
print(result)