'''
Time of Flight: The total duration (in seconds) that a projectile 
remains in the air before hitting the target or ground.
Formula: T = (2 * u * sin(theta)) / g
'''

# Import necessary module
import math

# Input values
velocity = float(input("Enter the velocity (u) in m/s:"))
theta=float(input("Enter theta (In Degrees):"))

# Acceleration due to gravity (in m/s^2)
g=9.8

# Convert angle from degrees to radians
radians=math.radians(theta)

# Calculate Time of Flight
T=(2*velocity*math.sin(radians))/g

# Output the result
print(f'Time of Flight (T) is: {T:.2f} seconds')