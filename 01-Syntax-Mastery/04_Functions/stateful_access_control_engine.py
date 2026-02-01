"""
Stateful Access Control Engine

Determines system access based on
role, verification status, and failed attempts
"""

role = input("Enter role (admin/user/guest): ").strip().lower()
attempts = int(input("Enter failed attempts: "))
verified = input("Identity verified? (yes/no): ").strip().lower()

def check_attempts(attempts):
    if attempts >= 5:
        return "Access Blocked: Too Many Attempts"
    return None

def check_verification(verified):
    if verified != "yes":
        return "Access Denied: Identity Not Verified"
    return None

def check_role(role):
    if role == "admin":
        return "Full Access Granted"
    elif role == "user":
        return "Limited Access Granted"
    elif role == "guest":
        return "Read-Only Access"
    return "Invalid Role"

def access_controller(role, attempts, verified):

    result = check_attempts(attempts)
    if result:
        return result
    result = check_verification(verified)
    if result:
        return result
    return check_role(role)

final = access_controller(role, attempts, verified)
print(f"System Response: {final}")