# Difference between regular methods, class methods and static methods

# Regular method -> Regular method in a class automatically take the instance as the first argument (self)

# class method -> Turn a regular method into a class method
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
