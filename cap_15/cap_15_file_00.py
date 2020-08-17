# Numpy

import numpy

# Create 3 arrays with numpy
n1 = numpy.arange(27)
n2 = numpy.arange(27)
n3 = numpy.arange(27)

print("n1: ", n1)
print("n2: ", n2)
print("n3: ", n3)
print("Type of numpy object:")
print(type(n1))  # n-dimensional array
print("____________________________________________________________________________________________________________")
print("Reshape arrays ")
n2 = n2.reshape(3, 9)      # 2-dimensional array
n3 = n3.reshape(3, 3, 3)   # 3-dimensional array
print("n1: ", n1)
print("n2: ", n2)
print("n3: ", n3)
print("____________________________________________________________________________________________________________")
# Create array from list entered manually
m = numpy.asarray([[123, 12, 123, 12, 33],[],[]])
print(m)
