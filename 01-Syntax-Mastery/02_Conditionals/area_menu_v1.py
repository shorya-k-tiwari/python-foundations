'''
Area Calculation Menu
'''

# Display menu
print('=== Area Calculation Menu ===')
print('1. Square')
print('2. Rectangle')
print('3. Triangle')
print('4. Circle')

# Get user choice
choice = input('Select a shape (1-4): ')

# Initialize area variable
if choice == '1':
    side = float(input('Enter the length of the square\'s side: '))
    area = side ** 2
    shape = 'Square'
elif choice == '2':
    length = float(input('Enter the length of the rectangle: '))
    width = float(input('Enter the width of the rectangle: '))
    area = length * width
    shape = 'Rectangle'
elif choice == '3':
    base = float(input('Enter the base of the triangle: '))
    height = float(input('Enter the height of the triangle: '))
    area = 0.5 * base * height
    shape = 'Triangle'
elif choice == '4':
    radius = float(input('Enter the radius of the circle: '))
    area = 3.14159 * radius ** 2
    shape = 'Circle'
else:
    print('Invalid choice')
    exit()
        
# Display the result
print(f'The area of the {shape} is {area}')