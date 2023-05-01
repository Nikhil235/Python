# While opening a file we can specify whether we are opening the file for 'readings', 'writing', 'reading & writing' or 'appending'

# Default -> reading

f = open('test.txt', 'w')  # opens a file for writing
print(f.name)  # Returns the name of the open file

f = open('test.txt', 'r+')  # Opens a file for reading and writing
print(f.mode)          # Mode in which it was opened
f = open('test.txt', 'a')  # Opens a file for appending

f = open('test.txt', 'r')  # Opens a file for reading

f.closed              # Returns whether the file associated with the variable is closed

# All files opened using an open() command need to be closed explicitly after their use is complete. If this is not done , we can end up with leaks that cause us to run over the maximum allowed file descriptors on the system and our app can throw an error.
f.close()

# Can avoid this problem using context manager

# 'with open()' ->  close the file as soon as the code has finished running or an error is thrown

with open('test.txt', 'r') as test_file:
    # code goes here
    text_file_contents = test_file.read()
    print(text_file_contents)

# print(f.read()) -> Produces the Error: ValueError: I/O operation on closed file

# Above Methods take a lot of storage as lines get stored in memory

with open('text.txt', 'r') as test_file:
    for line in test_file:
        print(line, end='')

# to read specific amount of text from the file
with open('test.txt', 'r') as test_file:
    text_file_contents = test_file.read(10)
    # No. of characters will be read and printed

    print(text_file_contents, end="")
    # When we reach the end of the file, read just reads what is left and returns an empty string


with open('text.txt', 'w') as text_file:
    size_to_read = 10
    text_file_contents = text_file.read(size_to_read)

    while len(text_file_contents) > 0:
        print(text_file_contents, end='')
        text_file_contents = text_file.read(size_to_read)

# filename.seek() sets the read position to whatever character we set it to. Here set to 0.
    text_file.seek(0)  # Sets the read position to 0
    print(text_file.tell())  # Prints 0


# Reads the first 10 characters. Read position set to 10
    text_file_contents = text_file.read(size_to_read)
    print(text_file.tell())  # Prints 10


# If we try to write to a file that is opened for reading. An error is produced.
# Error = 'io.UnsupportedOperation: not writable'
# with open('C:/#Personal/Coding Projects/Proj1/Py edn/text.txt', 'r') as text_file:
#     text_file.write('Test')

# If a file with this name doesn't already exist. It will be created.
# If a file does exist, it will be overwritten
with open('C:/#Personal/Coding Projects/Proj1/Py edn/text2.txt', 'w') as text_file:
    text_file.write('Test')


# Copying from one file to another, line by line
# This can't be done for image files. It shows an error. Invalid start byte. Copying an image file would require opening it in binary mode. We would be reading/writing bytes instead of text.
with open('C:/#Personal/Coding Projects/Proj1/Py edn/text.txt', 'r') as text_file:
    with open('C:/#Personal/Coding Projects/Proj1/Py edn/textcopy.txt', 'w') as copy_file:
        for line in text_file:
            copy_file.write(line)


# To read binary we change open(filename,'r') to open(filename, 'rb')
# To read binary we change open(filename,'w') to open(filename, 'wb')
# The below code with these changes, can copy an image file
with open('C:/#Personal/Coding Projects/Proj1/Py edn/text.txt', 'rb') as text_file:
    with open('C:/#Personal/Coding Projects/Proj1/Py edn/textcopy.txt', 'wb') as copy_file:
        for line in text_file:
            copy_file.write(line)


# Copying a file using chunks instead of line by line is better. This can be done by using the .read function we've studied above
with open('C:/#Personal/Coding Projects/Proj1/Py edn/text.txt', 'r') as text_file:
    with open('C:/#Personal/Coding Projects/Proj1/Py edn/textcopy.txt', 'w') as copy_file:
        chunk_size = 10
        chunk = text_file.read(chunk_size)
        while len(chunk) > 0:
            copy_file.write(chunk)
            chunk = text_file.read(chunk_size)
