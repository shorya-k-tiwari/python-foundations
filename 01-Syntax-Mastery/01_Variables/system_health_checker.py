# System Health Checker

cpu_usage=int(input("Enter CPU usage percentage (0-100): "))
memory_available=int(input("Enter available memory (in GB): "))
if cpu_usage < 70 and memory_available >= 8:
    print("System Status: Stable")
elif cpu_usage < 90 and memory_available >= 4:
    print("System Status: Under Load")
else:
    print("System Status: Critical")
