'''
Currency Converter
Converts an amount in INR to USD and EUR using fixed exchange rates
'''

inr = float(input("Enter amount in INR: "))

usd = inr / 83
eur = inr / 90

print(f"USD : {usd:.2f}")
print(f"EUR : {eur:.2f}")