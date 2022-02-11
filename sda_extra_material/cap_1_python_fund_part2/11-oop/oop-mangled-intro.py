class Animal:
    __name = ""  # mangled class variable, inaccessible
    __age = 0  # mangled class variable, inaccessible

    def __init__(self, name="Jenna", age=2):
        self.__name = name  # setting name when creating the object
        self.__age = age  # setting age when creating the object

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Age must be greater than 0.")

    def get_age(self):
        return self.__age


my_dog = Animal()
my_dog.set_age(3)  # sets the age
print(my_dog.get_age())  # gets the age
