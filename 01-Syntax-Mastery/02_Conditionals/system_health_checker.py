"""
System Health Checker

Evaluates system status based on CPU usage and available memory
"""

cpu = int(input("Enter CPU usage percentage (0-100): "))
memory = int(input("Enter available memory (in GB): "))

if cpu < 70 and memory >= 8:
    health = "Stable"
elif cpu < 90 and memory >= 4:
    health = "Under Load"
else:
    health = "Critical"

print(f"System Status: {health}")