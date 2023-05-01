li = [9, 1, 8, 2, 7, 3, 6, 4, 5]

s_li = sorted(li)
print('Sorted Variable:\t', s_li)
# Sorted function -> Returns new sorted list to a variable

li.sort()
print('Original Variable:\t', li)
# Sorted Method -> sort the list and place. Returns none

# Descending order
s_li = sorted(li, reverse=True)
print('Descending sorted Variable:', s_li)

# Tuple don;t have sorted function
tup = (9, 1, 8, 2, 7, 3, 6, 4, 5)
s_tup = sorted(tup)
print('Tuple:\t', s_tup)

dictionary = {'name': 'Corey', 'job': 'Programming',
              'age': None, 'os': 'MacOS'}
s_di = sorted(dictionary)
print('Dictionary:\t', s_di)

li = [-6, -5, -4, 1, 2, 3]
s_li = sorted(li, key=abs)
print(s_li)


class Employee():
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __repr__(self):
        return f'{self.name}, {self.age}, ${self.salary}'


e1 = Employee('Carl', 37, 70000)
e2 = Employee('Sarah', 29, 80000)
e3 = Employee('John', 43, 90000)


employee = [e1, e2, e3]


def e_sort(emp):
    return emp.name


s_employees = sorted(employee, key=e_sort)

print(s_employees)
