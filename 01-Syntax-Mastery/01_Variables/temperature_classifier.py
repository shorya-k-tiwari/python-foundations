# Temperature Classifier

temperature = float(input("Enter temperature in Celsius: "))
if temperature >= 40:
    print("Extreme Heat")
elif 30 <= temperature < 40:
    print("Hot")
elif 20 <= temperature < 30:
    print("Warm")
elif 10 <= temperature < 20:
    print("Cool")
else:
    print("Cold")
