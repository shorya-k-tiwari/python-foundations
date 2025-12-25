'''
Profile Statistics Calculator
'''

# Personal information
name = "Shorya"
age = 16

# Study schedule details
daily_study_hours = 8.0
years_to_target = 1

# Discipline status
is_disciplined = True

# Calculate total study hours over the target period
total_study_hours = daily_study_hours * 365 * years_to_target

# Display profile statistics
print("===== Profile Statistics =====")
print(f"Name               : {name}")
print(f"Age                : {age} years")
print(f"Daily Study Hours  : {daily_study_hours} hrs")
print(f"Total Study Hours  : {total_study_hours:.2f} hrs")
print(f"Disciplined        : {is_disciplined}")
print("==============================")