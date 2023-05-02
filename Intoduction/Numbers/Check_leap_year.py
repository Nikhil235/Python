# Check whether a year is leap year or not.

# year = 2000

year = int(input("Enter a year: "))

# divided by 100 -> century year
# century year divided by 400 is leap year

if year % 400 == 0 and year % 100 == 0:
    print(f'{year} is a leap year.')

# not divided by 100 -> not a century year
# year divided by 4 -> leap year

elif year % 4 == 0 and year % 100 != 0:
    print(f'{year} is a leap year.')

else:
    print(f'{year} is not a century year.')
