"""
Digit to Word Converter

Converts a single digit (0-9) into its English word representation
"""

n = int(input("Enter a digit (0-9): "))

if n == 0:
    word = "Zero"
elif n == 1:
    word = "One"
elif n == 2:
    word = "Two"
elif n == 3:
    word = "Three"
elif n == 4:
    word = "Four"
elif n == 5:
    word = "Five"
elif n == 6:
    word = "Six"
elif n == 7:
    word = "Seven"
elif n == 8:
    word = "Eight"
elif n == 9:
    word = "Nine"
else:
    word = None

if word is not None:
    print(word)
else:
    print("Invalid digit. Please enter a number between 0 and 9")