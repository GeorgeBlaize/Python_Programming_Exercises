
# Python Program to Find Hash of File

import hashlib
def hash_file(filename):

    h=hashlib.sha1()

    with open(filename,'rb')as file:

        chunk =0
        while chunk !=b'':
            chunk =file.read(1024)
            h.update(chunk)

    return h.hexdigest()

message=hash_file("Phineas_Sings_Green_Day_s_21_Guns.mp3")
print(message)
