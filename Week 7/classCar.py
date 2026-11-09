# Samat
# 11/8/2026
# Problem 6 - The car class with two new attributes, type and manufacturer,
# their methods, and an updated fullSpecs() method.
#
# Attribute vs. method:
# - An attribute is a piece of data that belongs to an object, like
#   self.model or self.color. It describes what the object HAS.
# - A method is a function defined inside the class, like getModel() or
#   fullSpecs(). It describes what the object can DO, and it is called
#   with dot notation and parentheses, like car1.getModel().

class car:

    def __init__(self, model, year, color, type, manufacturer):
        # Attributes - the data each car object stores
        self.model = model
        self.year = year
        self.color = color
        self.type = type
        self.manufacturer = manufacturer

    # Methods - the actions each car object can do
    def getModel(self):
        return self.model

    def getYear(self):
        return self.year

    def getColor(self):
        return self.color

    def getType(self):
        return self.type

    def getManufacturer(self):
        return self.manufacturer

    def fullSpecs(self):
        return (self.manufacturer + ' ' + self.model + ' ' + str(self.year) + ' '
                + self.color + ' ' + self.type)

car1 = car("Sports", 2012, "Blue", "Coupe", "Chevrolet")
car2 = car("Sedan", 2020, "Black", "Electric", "Tesla")

print(car1.getColor())
print(car1.getModel())
print(car2.getColor())
print(car1.getType())
print(car2.getManufacturer())
print(car1.fullSpecs())
print(car2.fullSpecs())
