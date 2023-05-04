# How to handle errors and exceptions in Python
# Error -> issue in a program that prevents the program from completing its task.
# Exception -> condition that interrupts the normal flow of the program.
# Both Errors and exceptions are type of runtime error(occur during execution of a program).
# Syntax ->
# try:
#     pass
# except Exception:
#     pass
# else:
#     pass
# finally:
#     pass

# try and except Statement
# x is not define, so it will run the except statement and print the warning.
try:
    print(x=0)
except:
    print("An exception has occurred!")


# Multiple except statement example

try:
    print(1/0)
except ZeroDivisionError:
    print("You cannot divide a value with zero")
except:
    print("Something else went wrong")

# File example
try:
    with open('test_file.txt') as file:
        read_data = file.read()
except FileNotFoundError as fnf_error:
    print(fnf_error)
    print("Explanation: We cannnot load the 'test_file.txt' file")


# try with else Clause
try:
    result = 1/3
except ZeroDivisionError as err:
    print(err)
else:
    print(f"Your answer is {result}")

# IndexError with else example
x = [5, 8, 9, 13]


def find_nth_value(x, n):
    try:
        result = x[n]
    except IndexError as err:
        print(err)
    else:
        print("Your answer is ", result)


find_nth_value(x, 6)
find_nth_value(x, 2)


# finally keyword in python
def divide(x, y):
    try:
        result = x/y
    except ZeroDivisionError:
        print("Please change 'y' argument to non-zero value")
    except:
        print("Something went wrong")
    else:
        print(f"Your answer is {result}")
    finally:
        print("\033[92m Code by Nikhil\033[00m")


divide(1, 0)
divide(3, 4)
# divide(1, g)
