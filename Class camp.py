class Vehicle:
    def __init__(self, name, colour, kind, value) -> None:
        self.name = name
        self.kind = kind
        self.colour = colour
        self.value = value
    def description(self):
        desc_str = "%s is a %s %s worth $%.2f" % (self.name, self.colour, self.kind, self.value)
        return desc_str
   

car1 = Vehicle("Fer", "red, convertible", 60,000.00)
car2 = Vehicle("Jump", "blue, van", 10,000.00)

print(car1.description())
print(car2.description())
