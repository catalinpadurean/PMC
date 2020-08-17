# Python basics: operations with data types

monday_temperatures = [9.1, 8.8, 7.5]
monday_temperatures.append(8.3)
print(monday_temperatures)

print(monday_temperatures.index(7.5))
monday_temperatures.append(9.1)
monday_temperatures.append(9.1)
monday_temperatures.append(9.1)
monday_temperatures.append(2.1)

print(monday_temperatures)
print((monday_temperatures.index(9.1)))
print((monday_temperatures.index(9.1, 3, 10)))
print(monday_temperatures[:-2])
print(monday_temperatures[-2:-1])
monday_temperatures.append("temperature")
print(monday_temperatures)
print(monday_temperatures[-1][-5:])
student_grades = {"Mary": 2.4, "Jon": 4.9, "X": 8.8}
print(student_grades["X"])


########################################################################################################################
#In this section you learned that:

#Lists, strings, and tuples have a positive index system:

["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
#  0      1      2      3      4      5      6
#And a negative index system:

["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
#  -7     -6     -5     -4     -3     -2     -1
#In a list, the 2nd, 3rd, and 4th items can be accessed with:

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
days[1:4]
#Output: ['Tue', 'Wed', 'Thu']
#First three items of a list:

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
days[:3]
#Output:['Mon', 'Tue', 'Wed']
#Last three items of a list:

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
days[-3:]
#Output: ['Fri', 'Sat', 'Sun']
#Everything but the last:

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
days[:-1]
#Output: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']
#Everything but the last two:

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
days[:-2]
#Output: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
#A single in a dictionary can be accessed using its key:

phone_numbers = {"John Smith":"+37682929928","Marry Simpsons":"+423998200919"}
phone_numbers["Marry Simpsons"]
#Output: '+423998200919'





