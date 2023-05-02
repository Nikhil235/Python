# Factorial of a number is the product of all the integers from 1 to that number.
# 6! = 6*5*4*3*2*1 =720 (positve number)
# Factorial is not defined for negative numbers
# Factorial of zero is one ( 0! = 1 )

# Python program to find the factorial of a number provided by the user.

num = int(input("Enter a number: "))

factorial = 1

# check if the number is negative, positive or zero
if num < 0:
    print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1, num + 1):
        factorial = factorial * i
    print(f"The factorial of {num} is {factorial}")
