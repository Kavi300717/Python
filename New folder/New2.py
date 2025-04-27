class Car:
    def __init__(self, brand, model, available=True):
        self.brand = brand
        self.model = model
        self.available = available

    def rent(self):
        if self.available:
            self.available = False
            return f"{self.brand} {self.model} rented."
        else:
            return f"{self.brand} {self.model} is not available."

car1 = Car("BMW", "G60")
print(car1.rent())
# print(car1.rent())