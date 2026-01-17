"""
Quadratic Equation Generator

Generates a quadratic equation given its two roots
"""

r1 = float(input("Enter the first root: "))
r2 = float(input("Enter the second root: "))

b = -(r1 + r2)
c = r1 * r2

b_val = int(b) if b.is_integer() else b
c_val = int(c) if c.is_integer() else c

if b_val == 1:
    b_term = "+ x"
elif b_val == -1:
    b_term = "- x"
elif b_val > 0:
    b_term = f"+ {b_val}x"
elif b_val < 0:
    b_term = f"- {abs(b_val)}x"
else:
    b_term = ""

if c_val > 0:
    c_term = f"+ {c_val}"
elif c_val < 0:
    c_term = f"- {abs(c_val)}"
else:
    c_term = ""

print(f"x^2 {b_term} {c_term} = 0")