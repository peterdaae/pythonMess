class test_fun:

    def testing_print(name, greeting="Hello"):
        print(f"{greeting}, {name}")

    def sum(*args): #takes several arguments
        total = 0
        for num in args:
            total += num
        return total

    def print_user_info(**kwargs):
        for key, value in kwargs.items():
            print(f"{key}: {value}")

    def calculator(operation, x, y):
        return operation(x, y)

    def add(a, b):
        return a + b

    def subtract(a, b):
        return a - b

    def multiply(a, b):
        return a * b

    def divide(a, b):
        return a // b