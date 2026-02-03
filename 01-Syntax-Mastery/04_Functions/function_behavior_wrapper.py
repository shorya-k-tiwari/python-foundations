"""
Function Behavior Wrapper

Controls whether a function is allowed to execute
"""

def secure(action):
    permission = input("Enter access code: ")
    if permission != "OVERRIDE":
        print("Access Denied")
        return
    action()

def dangerous():
    print("System Core Modified")

def safe():
    print("Safe action executed")

print("1. Safe Action")
print("2. Dangerous Action")

choice = input("Choose action: ")

if choice == "1":
    safe()
elif choice == "2":
    secure(dangerous)
else:
    print("Invalid choice")