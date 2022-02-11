class Animal:
    name = ""  # class variable
    age = 0  # class variable

    def __init__(self, name="Jenna", age=2):  # special method used for instantiation - that is object creation
        self.name = name  # setting name when creating the object
        self.age = age  # setting age when creating the object

    def print_details(self):  # class method printing state of the instance
        print(f"Name: {self.name}, age: {self.age}")


my_dog = Animal()
my_dog.print_details()  # call function on particular object (my_dog)
print(my_dog.name)  # access particular object's field variable (my_dog)
my_dog.age = 3  # change particular object's field value (my_dog)

my_puppy = Animal()  # create my_puppy instance of Animal
my_older_dog = Animal()  # create my_older_dog instance of Animal
my_puppy.age = 1
my_puppy.name = "Rex Junior"
my_older_dog.age = 10
my_older_dog.name = "Rex Senior"

# prints out 'My puppy: Rex Junior, 1 and my older dog: Rex Senior, 10'
print(f"My puppy: {my_puppy.name}, {my_puppy.age} and my older dog: {my_older_dog.name}, {my_older_dog.age}")
