# Data analysis with Pandas

import pandas

pdf1 = pandas.DataFrame([[1, 2, 3], [10, 200, 40000], [-1, 0, -5]])
pdf2 = pandas.DataFrame([[1, 2, 3], [10, 200, 40000], [-1, 0, -5]], columns=["Price", "Age", "Value"])
pdf3 = pandas.DataFrame([[1, 2, 3], [10, 200, 40000], [-1, 0, -5]], columns=["Price", "Age", "Value"],index=["First", "Second", "Third"])
# print(pdf1)
# print(pdf2)
print(pdf3)

pdf4 = pandas.DataFrame([{"Name": "Jon", "Surname": "Johns"}, {"Name": "Jack"}])

# print(pdf4)

print(pdf1.mean().mean())
print(pdf3.Price)
print(type(pdf3.Price))
print(pdf3.Price.mean())
