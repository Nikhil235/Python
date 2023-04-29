# Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included). The numbers obtained should be printed in a comma separated sequence on a single line.

# use range(#begin, #end) method.
for i in range(2000, 3201):
    if i % 7 == 0 and i % 5 != 0:
        print(i, end=',')


# Using list comprehension
print(*(i for i in range(2000, 3201) if i % 7 == 0 and i % 5 != 0), end=',')


# Question 2
# Write a program which can compute the factorial of a given numbers.

# Solution  - (Using for loop)
n = int(input('Enter a number: '))

fact = 1
for i in range(1, n+1):
    fact = fact * i
print(fact)
