class Functions1:
    def power_of(self):
        x = int(input("Write the base (integer): "))
        y = int(input("Write the power (integer): "))
        result = x ** y
        print(f"{x} to the power of {y} is {result}")
        return result