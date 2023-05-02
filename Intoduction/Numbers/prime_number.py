# Check whether an integer is a prime number

# e.g.1 => using a flag variable

# num = 12

num = int(input("Enter a number: "))

# define a flag variable
flag = False

if num == 1:
    print(num, "is not a prime number")
elif num > 1:
    # Check for factors
    for i in range(2, num):
        if num % i == 0:
            # if factor is found, set flag to be true
            flag = True
            # break out of loop
            break

    # check if flag is True
    if flag:
        print(num, "is not a prime number")
    else:
        print(num, "is a prime number")


# E.g.2 => Using a for ... else statement
# num = 401

num = int(input("Enter a number: "))
if num == 1:
    print(num, "is not a prime number")
elif num > 1:
    for i in range(2, num):
        if num % i == 0:
            print(num, "is not a prime number")
            print(f'{i} times {num // i} is {num}')
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")
