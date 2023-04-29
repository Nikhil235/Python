# Python Program to check if a number is odd or even.

# Even number => perfectly divisible by 2.
#                Number % 2 == 0.

# Odd number => Remainder is 1, it is an odd number


number = int(input("Enter a number: "))
if (number % 2) == 0:
    print(f"{number} number is even")
else:
    print(f"{number} number is odd")
