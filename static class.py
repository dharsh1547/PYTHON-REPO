# STATIC METHOD IN PYTHON

class Calculator:

    # Static method
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        if b == 0:
            return "Cannot divide by zero"
        return a / b

# CALLING STATIC METHODS

print("Addition       :", Calculator.add(10, 5))
print("Subtraction    :", Calculator.subtract(10, 5))
print("Multiplication :", Calculator.multiply(10, 5))
print("Division       :", Calculator.divide(10, 5))