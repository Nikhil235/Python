# The standard form of a quadratic equation is
# ax2 + bx + c = 0, where
# a, b, c are real numbers and
# a != 0

# Quad equation
# (-b +- (b ** 2 - 4 * a * c) ** 0.5) / (2 * a * c)

# Solve the quadratic equation ax**2 + bx + c = 0

# import complex math module
import cmath

a = 1
b = 6
c = 5

# calculate the discriminant
d = (b ** 2) - (4 * a * c)

# Find two solutions
sol1 = (-b - cmath.sqrt(d)) / (2 * a)
sol2 = (-b + cmath.sqrt(d)) / (2 * a)

print(f"The Solution are {sol1} and {sol2}")
