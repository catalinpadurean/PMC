# Linkuri utile:
# 0. https://www.programiz.com/python-programming/property
# 1. https://realpython.com/primer-on-python-decorators/
class Animal:
    __name = ""  # mangled class variable, inaccessible
    __age = 0  # mangled class variable, inaccessible


    def __init__(self, name="Jenna", age=2):
        self.__name = name  # setting name when creating the object
        self.__age = age  # setting age when creating the object

    @property  # getter
    def age(self):
        return self.__age

    @age.setter  # setter
    def age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Age must be greater than 0.")

    @age.deleter  # deleter
    def age(self):
        del self.__age


my_dog = Animal()
my_dog.age = 3  # sets the age
print(my_dog.age)  # gets the age
