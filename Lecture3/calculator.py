from Lecture3.calculator_user_input import CalculatorUserInput

input = CalculatorUserInput
x = input.input_first
y = input.input_second
operation = input.input_operator

class Calculator:
    def calculator(self, operation, x, y):
        return operation(x, y)

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        return a / b