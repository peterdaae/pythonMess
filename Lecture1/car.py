class Car:

    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def drive(self):
        print("Driving " + self.make + " car")

    def stop(self):
        print("Stopping " + self.make + " car")


    def checkCar(self):
        if self.year >= 2000:
            print("Car is new from " + str(self.year))
        else:
            print("Car is old from " + str(self.year))






