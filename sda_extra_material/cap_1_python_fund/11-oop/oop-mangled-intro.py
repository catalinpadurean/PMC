
class Animal:
    __name = ""  # mangled class variable, inaccessible
    __age = 0    # mangled class variable, inaccessible

    def __init__(self, name="Jenna", age=7854322):
        self.__name = name  # setting name when creating the object
        self.__age = age  # setting age when creating the object

    def set_age(self, age):
        if age > 0:
            self.__age = age
            print("Success! You changed the __age field")
        else:
            print("Age must be greater than 0.")

    def get_age(self):
        return self.__age



my_dog = Animal()
my_dog.set_age(-100)  # sets the age
print(my_dog.get_age()) # sets the age
my_dog.set_age(100)  # sets the age
print(my_dog.get_age()) # sets the age
print(my_dog.__name)
print(my_dog.__age)

# print(my_dog.get_age())  # gets the age

#
# class Parent:
#     def __init__(self):
#        self.__help("will take child to school")
#     def help(self, activities):
#         print("parent",activities)
#
#     #help = help   # private copy of original help() method
#     __help = help   # private copy of original help() method
# class Child(Parent):
#     def help(self, activities, days):   # notice this has 3 arguments and overrides the Parent.help()
#         self.activities = activities
#         self.days = days
#         print ("child will do",self.activities, self.days)


# the goal was to extend and override the Parent class to list the child activities too
# print ("list parent & child responsibilities")
# c = Child()
# c.help("laundry","Saturdays")
#
# class Me(object):
#     def override_me(self):
#         print ("Me: I should NOT be called")
#
#     def __dont_override_me(self):
#         print ("Me: I SHOULD be called")
#
# class OverrideMe(Me):
#     def override_me(self):
#         print ("OverrideMe: I SHOULD be called")
#
#     def __dont_override_me(self):
#         print ("OverrideMe: I should NOT be called")
#
#
# me = Me()
# override = OverrideMe()

# me._Me__dont_override_me() # If you really want to call the method.
# me.__dont_override_me
# override.override_me()
# override._OverrideMe__dont_override_me()  # If you really want to call the method.
# override.__dont_override_me

