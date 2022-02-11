class Animal:
    name = ""
    age = 0

    def __init__(self, name="Jenna", age=2):
        self.name = name
        self.age = age


dog_a = Animal()
print(dog_a.name)  # prints out 'Jenna'
print(dog_a.age)
dog_b = dog_a
print(dog_b.name)  # prints out 'Jenna'
print(dog_b.age)
# print(dog_a.name)  # prints out 'Jenna'
# print(dog_b.name)  # prints out 'Jenna'
#
dog_a.name = "Changed value!"
print(dog_a.name)  # prints out 'Changed value!'
dog_b.name = "Another changed value"
print(dog_b.name)  # prints out 'Another changed value'
print(dog_a.name)
# print("La fel cum am observat in exercitiul optional din exercises_01_solved.py cu listele")
#
# # print(dog_a)
# # print(dog_b)
# dog_b.name = "X"
# print(dog_a.name)  # prints out 'Changed value!'
# print(dog_b.name)  # prints out 'Changed value!'


dog_a = 5
print(dog_a)
print(dog_b.name)
