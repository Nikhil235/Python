# Generators->
# A generator-function is defined like a normal function, but wheneveer it needs to generate a value,
#  it does so with the yield keyword rather than return. If the body of  a def contains yield,
#  the function automatically becomes a generator function

# Generators don't hold the entire result in memory it yields one result at a time\

# next value to yeild form a list

# Generator does not hold the entire result in memory

# for e.g.

# def square_numbers(nums):
#     for i in nums:
#         yield(i*i)


# my_nums = square_numbers([1, 2, 3, 4, 5])

# Using list comprehension
my_nums = (x*x for x in [1, 2, 3, 4, 5])

print(list(my_nums))

for num in my_nums:
    print(num)
