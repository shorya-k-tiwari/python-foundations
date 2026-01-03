'''
Student Result Calculator
'''

# Take subject-wise marks as input from the user
physics = int(input('Enter your marks in Physics (0-100): '))
chemistry = int(input('Enter your marks in Chemsitry (0-100): '))
maths = int(input('Enter your marks in Mathematics (0-100): '))
cs = int(input('Enter your marks in Computer Science (0-100): '))
english = int(input('Enter your marks in English (0-100): '))

# Calculate total marks obtained
total = physics + maths + chemistry + cs + english

# Calculate average marks
average = total / 5

# Calculate percentage based on total marks
percentage = (total / 500) * 100

# Display the results
print(f'Total marks: {total}/500')
print(f'Average marks: {average}')
print(f'Percentage: {percentage}%')