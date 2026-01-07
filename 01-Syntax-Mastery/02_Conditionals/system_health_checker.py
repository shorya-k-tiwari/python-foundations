''' 
System Health Checker

System Health Checker assesses and monitors the status 
of a system's components for performance, errors, or issues
'''

# Get user input for CPU usage and available memory
cpu=int(input("Enter CPU usage percentage (0-100): "))
memory=int(input("Enter available memory (in GB): "))

# Store evaluated system health status
health = ""

# Evaluate system health based on CPU and memory
if cpu < 70 and memory >= 8:
    health = "Stable"
elif cpu < 90 and memory >= 4:
    health = "Under Load"
else:
    health = "Critical"

# Output the system health status
print(f"System Status: {health}")