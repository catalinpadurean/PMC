# define the Vehicle class
class Vehicle:
    name = ""
    type = ""
    color = ""
    price = 0.0

    def __init__(self, name, price, type="Sedan", color="White"):
        self.name = name
        self.price = price
        self.type = type
        self.color = color

    def description(self):
        return f"{self.name} is a {self.color} {self.type} worth {self.price}."


vehicles = []

for i in range(3):
    name = input("Please provide name: ")
    price = input(f"Please provide {name}'s price: ")
    decision = input("Do you want to specify type and color?")
    if decision == "yes":
        type = input(f"Please provide {name}'s type: ")
        color = input(f"Please provide {name}'s color: ")
        vehicles.append(Vehicle(name, price, type=type, color=color))
    else:
        vehicles.append(Vehicle(name, price))

for vehicle in vehicles:
    print(vehicle.description())
