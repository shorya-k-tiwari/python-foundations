"""
Fibonacci Sequence Generator

Generates the first n terms of the Fibonacci sequence using iteration
"""

n = int(input("Enter how many terms: "))

if n <= 0:
    result = "Invalid input: n must be greater than 0"
else:
    previous, current = 0, 1
    sequence = []

    for i in range(n):
        sequence.append(str(previous))
        previous, current = current, previous + current

    result = "Fibonacci Sequence: " + " ".join(sequence)

print(result)