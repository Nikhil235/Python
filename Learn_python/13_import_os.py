import os
from datetime import datetime
# import os -> module allows us to access functionality of the underlying operating system.
# print(dir(os))

# print(os.getcwd())  # Get current working directory

# os.chdir('/usr/local/bin')  # Change current working directory

# to make a directory (folder or file)
os.mkdir('OS-Demo-2')  # to make a directory
os.makedirs()    # to make sub folder

# to delete a directory
os.rmdir()
os.removedirs()

# print(os.listdir())  # List directory

# to rename a directory
os.rename('#Origina name file', 'New file name')

# Information about file
os.stat('File name')
# to check size of the file
os.stat('File size').st_size
# to check last modification time of the file
# os.stat('File modification time').st_mtime
# to read in human readble format
# import time
# mod_time = os.stat('File modification time').st_mtime
# print(datetime.fromtimestamp(mod_time))

# traverse directory recursively
# for dirpath, dirnames, filename in os.walk('os.path.'):
# print('Current path': dirpath)
# print('Directories:, dirpath')
# print('Files:': filenames)

# to get environment variables
print(os.environ.get('HOME'))

# to combine home directory to a file name
# join path without worrying about/
file_path = os.path.join(os.environ.get("HOME"), 'test.txt')
print(file_path)

# get basename
print(os.path.basename('path-name'))

# get dirname first and directory name second
print(os.path.split('pathname with file name'))

# check if the path exists or not
os.path.exists(file_path)('file_path')

# split path and file extension
os.path.splitext(file_path)

# check what methods exist
dir(os)
