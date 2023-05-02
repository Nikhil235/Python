# Python program to find the largest number among the three input numbers

# num1 = 45
# num2 = 75
# num3 = 41

num1 = float(input("Enter first Number: "))
num2 = float(input("Enter second Number: "))
num3 = float(input("Enter third Number: "))

if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num3 and num2 >= num3:
    largest = num2
else:
    largest = num3

print("The largest number is", largest)
