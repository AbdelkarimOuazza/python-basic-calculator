def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero."
    return a / b

print("=== Simple Python Calculator ===")

try:
    num1 = float(input("Enter first number: "))
    operator = input("Choose an operator (+, -, *, /): ")
    num2 = float(input("Enter second number: "))

    if operator == "+":
        print("Result:", add(num1, num2))
    elif operator == "-":
        print("Result:", subtract(num1, num2))
    elif operator == "*":
        print("Result:", multiply(num1, num2))
    elif operator == "/":
        print("Result:", divide(num1, num2))
    else:
        print("Error: Invalid operator.")

except ValueError:
    print("Error: Please enter a valid number.")