'''
Simple Calculator

This program performs basic arithmetic operations
'''

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "cant divide by zero"
    else:
        return a / b

def power(a, b):
    result = 1
    for i in range(b):
        result = result * a
    return result

def factorial(n):
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result

def show_menu():
    print("\n--- Calculator ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Factorial")
    print("7. Exit")

def calculator():
    while True:
        show_menu()
        choice = input("\nEnter choice: ")
        
        if choice == '7':
            print("See you again!")
            break
        
        if choice in ['1', '2', '3', '4', '5']:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
            
            if choice == '1':
                print("Result:", add(num1, num2))
            elif choice == '2':
                print("Result:", subtract(num1, num2))
            elif choice == '3':
                print("Result:", multiply(num1, num2))
            elif choice == '4':
                print("Result:", divide(num1, num2))
            elif choice == '5':
                print("Result:", power(num1, int(num2)))
        
        elif choice == '6':
            num = int(input("Enter number: "))
            print("Result:", factorial(num))
        
        else:
            print("invalid choice")

calculator()