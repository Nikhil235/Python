# Class variables -> Variables that are shared among all instances of a class
# class variables should be the same for each instance of a class
# At the class level, variables are referred to as class variables

# One of the principles of software development is the DRY principle,
# which stand for don't repeat yourself. This principle is geared towords limiting repetition within code,
# and object-oriented programming adheres to the DRY principle as it reduces redundancy.

class Employee:

    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = f'{first}.{last}@Company.com'

        Employee.num_of_emps += 1

    def fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


emp_1 = Employee('Nikhil', 'Arjun', 50000)
emp_2 = Employee('Test', 'User', 60000)


Employee.raise_amount = 1.05  # Change the raise amount to 1.05 of all Employee

emp_1.raise_amount = 1.06
print(emp_1.__dict__)

# print(emp_1.__dict__)
# print(Employee.__dict__)
# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

print(Employee.num_of_emps)
