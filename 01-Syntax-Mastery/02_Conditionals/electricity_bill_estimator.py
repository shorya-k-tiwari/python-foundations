"""
Electricity Bill Estimator
Calculates total cost based on simplified slab-wise unit rates
"""

units = float(input("Enter the number of electricity units consumed: "))

if units <= 100:
    cost = units * 2.0
elif units <= 300:
    cost = units * 3.0
else:
    cost = units * 5.0

print(f"Total electricity bill: ₹{cost}")