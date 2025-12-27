''' User Information and Calculations '''

# Read user information from input
name = input('Enter Your Name:')
age = int(input('Enter Your Age (in years):'))
height = float(input('Enter Your Height (in meters):'))

# Compute additional info (months, days, height in cm)
months = age * 12
days = age * 365
cm = height * 100

# Display types of the variables 
print(f"Type of name: {type(name)}")
print(f"Type of age: {type(age)}")
print(f"Type of height: {type(height)}")

# Display user information summary
print("\n---User Information Summary---")
print(f'Hello {name}!')
print(f'You are {age} years old which is approximately {months} months or {days} days')
print(f'Your height is {height} meters which is {cm} centimeters')