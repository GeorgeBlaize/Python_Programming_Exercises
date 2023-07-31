
# Python Program to Safely Create a Nested Directory
import os

try:
    os.makedirs("/dirA/dirB")
except FileExistsError:
    print("File already exists")
