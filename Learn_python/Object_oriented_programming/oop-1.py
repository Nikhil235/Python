# Python Object-Oriented Porgramming

# Classes -> used throughout most modern programming languages
# Logically group our data and functions in way that's easy to[reuse] and also easy to build upon if need be
# Data and functions that are associated with specific class call those attributes and methods.

# Methods -> function that is associated with specific class

# Class is basically a blueprint for creating instances

# instance variables -> variable contain data that is unique to each instance(define inside a method and belong to the current instance of a class)

# __init__ method -> initialize (in other lang its constructor)
# Now when we create methods within a class they receive the instance as the first argument automatically

class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f'{first}.{last}@Company.com'

    def fullname(self):
        return f'{self.first} {self.last}'


emp_1 = Employee('Nikhil', 'Arjun', 50000)
emp_2 = Employee('Test', 'User', 60000)

print(emp_1.email)
print(emp_2.email)

print(f'{emp_1.first} {emp_1.last}')
print(emp_1.fullname())

emp_1.fullname()
print(Employee.fullname(emp_1))
