# A, B, and C are three sides of a triangle

# s = A + B + C / 2

# area =√(s(s-a)*(s-b)*(s-c))

# to find the area of the triangle
# a = 5
# b = 3
# c = 5

# Take inputs from the user
a = float(input("Enter first side: "))
b = float(input("Enter second side: "))
c = float(input("Enter third side: "))


# calculate the semi-perimeter
s = (a + b + c) / 2

# calculate the area of the triangle
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5

print(f'The area of the triangle is {area}')
