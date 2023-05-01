# Variable scope -> Understanding The LEGB rule and global/ nonlocal statement

# LEGB => Local, Enclosing, Global, Built-in

# def test():
# y = 'Local y'
# x = 'local x'
# print(y)
# print(x)


# test()
# print(y)   <= Can't run outside of the function (because it declared locally as a variable)

# import builtins


# def test(z):
#     x = 'local x'
#     print(z)


# test('local z')

# # built-in
# # print(dir(builtins))


# def my_min():
#     pass


# m = min([5, 1, 4, 2, 3])
# print(m)

# Enclosing (Nested function => )
def outer():
    x = 'outer x'

    def inner():
        nonlocal x
        x = 'inner x'
        print(x)

    inner()
    print(x)


outer()

# nonlocal x => allow us to work with local variables of enclosing function
