'''
Unit Conversion Pack

Converts distance and weight into commonly used measurement units
'''

distance = float(input('Enter distance in kilometers: '))
weight = float(input('Enter weight in kilograms: '))

meters = distance * 1000
miles  = distance * 0.621371

grams  = weight * 1000
pounds = weight * 2.20462

print("\nConversion Results")
print(f"Kilometers → Meters : {meters:.2f} m")
print(f"Kilometers → Miles  : {miles:.3f} mi")
print(f"Kilograms  → Grams  : {grams:.2f} g")
print(f"Kilograms  → Pounds : {pounds:.3f} lb")