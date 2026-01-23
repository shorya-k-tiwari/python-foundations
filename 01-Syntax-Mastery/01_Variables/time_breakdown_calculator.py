'''
Time Breakdown Calculator

Converts total seconds into hours, minutes, and seconds
'''

time = int(input("Enter time in seconds: "))

hours = time // 3600
minutes = (time % 3600) // 60
seconds = time % 60

print("\nTime Breakdown")
print(f"Hours   : {hours}")
print(f"Minutes : {minutes}")
print(f"Seconds : {seconds}")