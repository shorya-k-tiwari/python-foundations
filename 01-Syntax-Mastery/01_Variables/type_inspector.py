'''
Type Inspector 

Type Inspector is a simple script that collects user inputs, 
converts them to appropriate types, and prints each variable's value and data type
'''

# Collect user input values
name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height in meters: "))
student = input("Are you a student? (yes/no): ")

# Convert student response to boolean value
is_student = True if student.lower() == 'yes' else False

# Print variable values and types
print(f'Name -> {name} | Type: {type(name)}')
print(f'Age -> {age} | Type: {type(age)}')
print(f'Height -> {height} | Type: {type(height)}')
print(f'Student -> {is_student} | Type: {type(is_student)}')