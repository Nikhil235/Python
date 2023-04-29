# Swap two variables by using a temporary variable, without using temporary variable.

# Python program to swap two variables
# x = 8
# y = 6

# To take inputs from the user
x = input('Enter value of x: ')
y = input('Enter value of y: ')

# Create a temporary variable and swap the values
# temp = x
# x = y
# y = temp

# print(f'The value of x after swapping : {x}')
# print(f'The value of y after swapping : {y}')


# Without Using Temporary Variable

x, y = y, x
print("x =", x, "y =", y)
