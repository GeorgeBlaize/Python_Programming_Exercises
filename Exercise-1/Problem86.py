
# Python Program to Get the Full Path of the Current Working Directory

import pathlib

print(pathlib.Path("my_file.txt").parent.absolute())

print(pathlib.Path().absolute())
