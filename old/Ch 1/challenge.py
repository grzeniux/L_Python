#Challenge: create a class to represent some information

class Car:
    def __init__(self, brand, model, body, year, horse_power, price) -> None:
        self.brand = brand
        self.model = model
        self.body = body
        self.year = year
        self.horse_power = horse_power
        self.price = price

    def get_description(self):
        return f"{self.brand}: {self.model}, {self.body}, {self.year}, {self.horse_power} -- {self.price} "

merc = Car("Mercedes", "C AMG", "Sedan", 2023, "530 km", "450 000 zł")
audi = Car("Audi", "RS6", "Avant", 2023, "650 km", "600 000 zł")

print(merc.get_description())
print(audi.get_description())