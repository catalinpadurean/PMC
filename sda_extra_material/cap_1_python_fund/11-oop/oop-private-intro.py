class Animal:
    _name = ""  # private class variable, still accessible
    _age = 0  # private class variable, still accessible

    def __init__(self, name="Jenna", age=2):  # special method used for instantiation - that is object creation
        self._name = name  # setting name when creating the object
        self._age = age  # setting age when creating the object

    def print_details(self):  # class method printing state of the instance
        print(f"Name: {self._name}, age: {self._age}")

my_dog = Animal.__init__()


