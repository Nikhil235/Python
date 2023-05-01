from datetime import datetime
person = {'name': "Jenn", "age": 23}

# sentence = 'My name is ' + person['name'] +
# ' and I am ' + str(person.[age]) + ' years old'

# formatted string
# sentence = 'My name is {} and I am {} years old.'.format(
#     person['name'], person['age'])
# print(sentence)

# f-string
first_name = 'Corey'
last_name = 'Schafer'

# sentence = 'My name is {} {}'.format(first_name, last_name)
# sentence = f'My name is {first_name.upper()} {last_name.upper()}'
# print(sentence)

person = {'name': 'jenn', 'age': 23}

# # Formatted-string on dictionary
# sentence = 'My name is {} and I am {} years old'.format(
#     person['name'], person['age'])
# print(sentence)

# F-string on dictionary
# sentence = f"My name is {person['name']} and I am {person['age']} years old"
# print(sentence)

# calculation = f'4 times 11 is equal to {4 * 11}'
# print(calculation)

# for n in range(1, 11):
#     sentence = f'The value is {n:02}'
#     print(sentence)

# pi = 3.14159265
# sentence = f'The value is {pi:.4f}'
# print(sentence)


# birthday = datetime(1997, 2, 5)

# sentence = f'Jenn has a birthday on {birthday:%B %d, %Y}'
# print(sentence)

def quick_sort(seq):
    length = len(seq)

    if length <= 1:
        return seq
    else:
        pivot = seq.pop()

    more = []
    less = []

    for val in seq:
        if val > pivot:
            more.append(val)
        else:
            less.append(val)

    return quick_sort(less) + [pivot] + quick_sort(more)


print(quick_sort([1, 3, 4, 23, 7, 4, 6, 8, 9, 5, 4, 8]))
