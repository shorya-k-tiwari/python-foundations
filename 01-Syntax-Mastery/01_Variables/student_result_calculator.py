"""
Student Result Calculator
Accepts subject-wise marks and computes total, average, and percentage
"""

physics = int(input("Enter your marks in Physics (0-100): "))
chemistry = int(input("Enter your marks in Chemistry (0-100): "))
maths = int(input("Enter your marks in Mathematics (0-100): "))
cs = int(input("Enter your marks in Computer Science (0-100): "))
english = int(input("Enter your marks in English (0-100): "))

total = physics + chemistry + maths + cs + english
average = total / 5
percentage = (total / 500) * 100

print(f"Total Marks      : {total} / 500")
print(f"Average Marks    : {average:.2f}")
print(f"Percentage       : {percentage:.2f}%")