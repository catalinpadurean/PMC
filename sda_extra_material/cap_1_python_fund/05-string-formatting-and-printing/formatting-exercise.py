header_name = "Name"
header_age = "Age"
header_salary = "Salary"

print(f"| {header_name:15} | {header_age:5} | {header_salary:12} |")
print("-" * 42)

name = "John Doe"
age = 27
salary = 123456
print(f"| {name:15} | {age:5} | {salary:12.2f} |")

name = "John Wick"
age = True
salary = 50000.002
print(f"| {name:15} | {age:5} | {salary:12.2f} |")

name = "Jeff Bezos"
age = 45
salary = 999999999.95
print(f"| {name:15} | {age:5} | {salary:12.2f} |")
