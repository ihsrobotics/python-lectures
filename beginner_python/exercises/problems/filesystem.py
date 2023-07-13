# use dataclass
# use abstract method

# Part 1)
# create an abstract DiskObject class
# that has:
# * a property and abstract method `size()` that returns the size of the object on the disk
# * an `__init__` method that takes a name (str) and a date created (datetime)
#   and stores those (use dataclasses for this)

# Part 2)
# create a File class that inherits from DiskObject
# that has:
# * an `__init__` method that takes a name, date created, and file size (int)
# * a `size` property getter that returns the file size
# * a `size` setter that modifies the file size only if the new size is an integer >= 0, else raises a ValueError

# Part 3)
# create a Directory class that inherits from DiskObject
# that has:
# * an `__init__` method that takes a name, date created, and as many DiskObject objects as are provided. It should
#   store the provided DiskObject objects in a list `children`
# * a `size` property getter that returns the sum of all the children DiskObjects' size

# necessary imports
from abc import ABC, abstractmethod
from dataclasses import dataclass
from datetime import datetime

# Your code here!
pass

# the below code should run when you finished parts 1 through 3
# cool_image = File("image.png", datetime.now(), 128000)
# print(cool_image.size)
#
# text_file = File("text.txt", datetime.now(), 1000)
# text_file.size = 2000  # this should work
# try:
#     text_file.size = -1000  # this should raise an exception caught by the except clause
# except ValueError:
#     print("correctly stopped user from trying to resize text file to negative size")
#
# first_directory = Directory("directory", datetime.now(), cool_image, text_file)
# print(
#     first_directory.size
# )  # this should be equivalent to cool_image.size + text_file.size
# print(first_directory.children)
#
# second_directory = Directory(
#     "/",
#     datetime.now(),
#     File("temp.b", datetime.now(), 100),
#     File("other.b", datetime.now(), 247),
#     first_directory,  # since `Directory`s are `DiskObjects`, this should work
# )
# print(second_directory.size)
