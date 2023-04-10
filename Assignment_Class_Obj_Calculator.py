class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, x, y):
        self.result = x + y

    def subtract(self, x, y):
        self.result = x - y

    def multiply(self, x, y):
        self.result = x * y

    def divide(self, x, y):
        self.result = x / y


calculator = Calculator()

operation = input("What operation would you like to perform? (+, -, *, /): ")

if operation == "+":
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))
    calculator.add(x, y)
elif operation == "-":
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))
    calculator.subtract(x, y)
elif operation == "*":
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))
    calculator.multiply(x, y)
elif operation == "/":
    x = float(input("Enter first number: "))
    y = float(input("Enter second number: "))
    calculator.divide(x, y)

print(f"The result is {calculator.result}")