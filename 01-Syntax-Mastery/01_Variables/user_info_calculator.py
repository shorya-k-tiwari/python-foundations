# User Information and Calculations

name = input('Enter Your Name:')
age = int(input('Enter Your Age (in years):'))
height = float(input('Enter Your Height (in meters):'))
months = age * 12
days = age * 365
cm = height * 100
print(f"Type of name: {type(name)}")
print(f"Type of age: {type(age)}")
print(f"Type of height: {type(height)}")
print("\n---User Information Summary---")
print(f'Hello {name}!')
print(f'You are {age} years old which is approximately {months} months or {days} days')
print(f'Your height is {height} meters which is {cm} centimeters')