class CarGas:
    def car_gas(self):
        gallons = float(input("How many gallons?"))
        fuel_efficiency = float(input("How many miles per gallon?"))
        price_gallon = float(input("Price per gallon?"))

        cost_100_miles = (100 / fuel_efficiency) * price_gallon

        distance_travel = gallons * fuel_efficiency

        print(f"Cost per 100 miles is: {cost_100_miles}")
        print(f"Distance possible to travel: {distance_travel}")
