'''
Speed Calculator

Calculates speed using distance and time
'''

distance = float(input("Enter distance in kilometers: "))
time = float(input("Enter time in hours: "))

speed = distance / time

print(f"Speed: {speed:.2f} km/h")