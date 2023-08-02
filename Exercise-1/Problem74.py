
# Python Program to Extract Extension From the File Name

import os
file_details = os.path.splitext('/path/file.ext')
print(file_details)
print(file_details[1])
