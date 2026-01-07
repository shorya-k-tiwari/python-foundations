'''
Temperature Classifier 

Temperature classifier categorizes temperatures into levels like freezing,
cold, cool, warm, hot, or extreme using defined thresholds
'''

# Read temperature in Celsius from the user
temperature = float(input("Enter temperature in Celsius: "))

# Store temperature classification
classify = ""

# Determine classification based on Celsius temperature ranges
if temperature >= 40:
    classify = "Very Hot"
elif 30 <= temperature < 40:
    classify = "Hot"
elif 20 <= temperature < 30:
    classify = "Warm"
elif 10 <= temperature < 20:
    classify = "Cool"
else:
    classify = "Cold"

# Display the temperature classification
print(f'Temperature Classification: {classify}')