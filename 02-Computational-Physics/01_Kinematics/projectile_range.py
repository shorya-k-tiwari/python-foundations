'''
Projectile Range Calculator
Range is the total horizontal distance traveled by an object (projectile) 
along the ground from its starting point to the point where it hits the ground again
Formula: R = (v^2 * sin(2 * theta)) / g
Note: Maximum range is achieved when theta = 45 degrees
'''

# Import math module for trigonometric calculations
import math

# Input values
u = float(input("Enter the initial velocity (m/s): "))
theta = float(input("Enter the launch angle (degrees): "))

# Convert angle from degrees to radians
radians = math.radians(theta)

# Acceleration due to gravity (in m/s^2)
g = 9.81

# Calculate Projectile Range
R = (u**2 * math.sin(2 * radians)) / g

# Output the result
print(f"The projectile range is: {R:.2f} meters") 