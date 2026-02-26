class ProgrammingNumbersStrings:
    def userNameInput(self):
        print("What is your weight in KG: ")
        weightInput = input()
        weightFormatted = float(weightInput)
        weightPounds = weightFormatted * 2.2
        print(f"Your weight in pounds is: {weightPounds:.2f}")

    def userAgeInput(self):
        currentYear = 2026
        print("What year were you born?")
        yearInput = input()
        yearFormat = int(yearInput)
        age = currentYear - yearFormat
        print("You age is: " + str(age))

    def radiusInputCircle(self):
        pi = 3.14
        try:
            radiusInput = input()
            radiusFormat = float(radiusInput)
            area = pi * (radiusFormat ** 2)
            circumference = 2 * pi * radiusFormat
            print(f"Area of the circle: {area}")
            print(f"Circumference of the circle: {circumference}")
        except ValueError:
            print("Invalid input")

    def radiusInputSphere(self):
        pi = 3.14
        try:
            print("Input the radius")
            radiusInput = input()
            radiusFormat = float(radiusInput)
            volume = (4/3) * pi * (radiusFormat ** 3)
            area = 4 * pi * (radiusFormat ** 2)
            print(f"Volume of the sphere: {volume}")
            print(f"Surface area of the sphere : {area}")
        except ValueError:
            print("Invalid Input")


