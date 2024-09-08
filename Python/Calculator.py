import math
import cmath

def basic_operations(a, b, operation):
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    elif operation == '/':
        return a / b if b != 0 else "Error: Division by zero"
    else:
        return "Invalid Operation"

def advanced_operations(a, operation):
    if operation == 'sqrt':
        return math.sqrt(a)
    elif operation == 'log':
        return math.log(a)
    elif operation == 'exp':
        return math.exp(a)
    elif operation == 'sin':
        return math.sin(a)
    elif operation == 'cos':
        return math.cos(a)
    elif operation == 'tan':
        return math.tan(a)
    elif operation == 'complex_sqrt':
        return cmath.sqrt(a)
    else:
        return "Invalid Advanced Operation"

def complex_calculator():
    while True:
        print("\nChoose mode: Basic or Advanced or Complex?")
        mode = input("Mode (basic/advanced/complex): ").lower()

        if mode == 'basic':
            a = float(input("Enter first number: "))
            operation = input("Enter operation (+, -, *, /): ")
            b = float(input("Enter second number: "))
            result = basic_operations(a, b, operation)
            print(f"Result: {result}")

        elif mode == 'advanced':
            a = float(input("Enter number: "))
            operation = input("Enter operation (sqrt, log, exp, sin, cos, tan): ").lower()
            result = advanced_operations(a, operation)
            print(f"Result: {result}")

        elif mode == 'complex':
            a = complex(input("Enter complex number: "))
            operation = input("Enter operation (complex_sqrt): ").lower()
            result = advanced_operations(a, operation)
            print(f"Result: {result}")

        else:
            print("Invalid mode!")
        
        continue_calculation = input("Do you want to perform another calculation? (y/n): ").lower()
        if continue_calculation != 'y':
            break

if __name__ == "__main__":
    complex_calculator()
