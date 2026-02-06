"""
Password Generator

Generates a secure random password of given length
"""

import random
import string

def generate_password(length):
    if length < 4:
        return "Length must be at least 4"

    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    chars = letters + digits + symbols
    password = [
        random.choice(letters),
        random.choice(digits),
        random.choice(symbols)
    ]
    password += random.choices(chars, k=length - 3)
    random.shuffle(password)
    return "".join(password)

def main():
    try:
        length = int(input("Enter password length: "))
        pwd = generate_password(length)
        print("Generated Password:", pwd)
    except ValueError:
        print("Enter a valid number")

if __name__ == "__main__":
    main()