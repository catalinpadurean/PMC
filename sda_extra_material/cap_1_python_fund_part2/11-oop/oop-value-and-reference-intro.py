class Animal:
    name = ""
    age = 0

    def __init__(self, name="Jenna", age=2):
        self.name = name
        self.age = age


dog_a = Animal()
dog_b = dog_a
print(dog_a.name)  # prints out 'Jenna'
print(dog_b.name)  # prints out 'Jenna'

dog_a.name = "Changed value!"
print(dog_a.name)  # prints out 'Changed value!'
print(dog_b.name)  # prints out 'Changed value!'
