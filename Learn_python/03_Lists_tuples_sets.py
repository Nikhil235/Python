# courses = ['History', 'Math', 'Physics', 'ComSci']
# courses_2 = ['Art', 'Education']
# nums = [1, 5, 2, 4, 3]
# print(courses)
# print(len(courses))
# print(courses[0])
# print(courses[3])
# print(courses[-1])
# print(courses[0:2])
# print(courses[:4])
# print(courses[2:])

# courses.append('Art')
# courses.insert(0, 'Art')
# courses.insert(0, courses_2)
# courses.extend(courses_2)
# courses.remove('Math')
# popped = courses.pop()  # Returns the removed value.
# print(popped)

# Sorted list
# courses.reverse()
# courses.sort(reverse=True)
# nums.sort(reverse=True)

# sorted_courses = sorted(courses)
# print(sorted_courses)
# print(sum(nums))

# print(courses.index('Math'))

# for index, course in enumerate(courses, start):
#     print(index, course)

# course_string = ' - '.join(courses)

# new_list = course_string.split(' - ')
# print(new_list)
# print(course_string)

# Tuples - similar to lists, but can't modify them

# Mutaable
# list_1 = ['History', 'Math', 'Physics', 'CompSci']
# list_2 = list_1

# print(list_1)
# print(list_2)

# list_1[0] = 'Art'

# print(list_1)
# print(list_2)

# Immutable
# tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
# tuple_2 = tuple_1

# print(tuple_1)
# print(tuple_2)

# tuple_1[0] = 'Art'

# print(tuple_1)
# print(tuple_2)

# Sets -> Similar to the tuples, but insted of () brackets it uses { } curly brackets

# cs_course = {'History', 'Math', 'Physics', 'CompSci', 'Math'}
# Sets throw away duplicate values
# art_course = {'History', 'Math', 'Art', 'Design'}

# print('Math' in cs_course)
# print(cs_course.intersection(art_course))
# print(cs_course.union(art_course))

# # Empty lists, tuple and sets
# empty_list = []
# empty_list = list()

# empty_tuple = ()
# empty_tuple = tuple()

# empty_set = {}  # This isn't right! It's a dictionary
# empty_set = set()

numbers = list(range(1, 6))
print(numbers)
