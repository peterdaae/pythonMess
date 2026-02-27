class Exercise1:
    def usernameInput(self):
        print("first name")

        firstName = input()
        charFirst = firstName[0]

        print("second name")

        secondName = input()
        charSecond = secondName[0]

        print("age")
        ageInput = input()
        age = int(ageInput)

        print("weight")
        weightInput = input()
        weight = float(weightInput)

        print("your name is " + firstName.upper() + " " + secondName.upper())
        print("Your initials are " + charFirst.upper() + charSecond.upper())
        print("Your age is " + str(age))
        print("Your weight is " + str(weight))

