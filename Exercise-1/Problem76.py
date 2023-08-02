
# Python Program to Get the Class Name of an Instance

class Vehicle:
    def __set_name__(self, name):
        return name

v=Vehicle()
print(v.__class__.__name__)
