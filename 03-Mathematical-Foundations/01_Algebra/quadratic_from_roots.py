''' 
Program to generate a quadratic equation from the given roots 
'''

# Taking roots of the quadratic equation as input from the user
r1 = float(input("Enter the first root: "))
r2 = float(input("Enter the second root: "))

# Compute coefficients using sum and product of roots
b = -(r1 + r2) 
c = r1 * r2 

# Formatting coefficients for display
b_str= int(b) if b.is_integer() else b
c_str= int(c) if c.is_integer() else c

# Format the x-term coefficient for clean equation display
if  b_str == 1:
    d = f"+ x"
elif b_str == 0:
    d = ""
elif b_str == -1:
    d = "- x"
elif b_str > 0:
    d = f"+ {b_str}x"
else:
    d = f"- {abs(b_str)}x"

# Formatting constant term
if c_str > 0:
    e = f"+ {c_str}"
elif c_str == 0:
    e = ""
else:
    e = f"- {abs(c_str)}"

# Displaying the quadratic equation
print(f"The quadratic equation is:\n x^2 {d} {e} = 0")