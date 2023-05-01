print('Imported my_module...')

test = 'Test String'


def find_index(to_serach, target):
    '''Find the index of a value in a sequence'''
    for i, value in enumerate(to_serach):
        if value == target:
            return i

    return -1
