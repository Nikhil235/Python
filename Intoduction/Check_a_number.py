# Python Program to check if a Number is Positive, Negative or 0


# Using if...elif...else
num = float(input("Enter a Number: "))
if num > 0:
    print("Postive Number")
elif num == 0:
    print("Zero")
else:
    print("Negative Number")


# Using Nested if
num = float(input("Enter a Number: "))
if num > 0:
    if num == 0:
        print("Zero")
    else:
        print("Positive Number")
else:
    print("Negative Number")
