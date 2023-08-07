
# Python Program to Find Factorial of Number

def factorial(num):
    if num==1:
        return num
    else:
        return num*factorial(num-1)

number=int(input("Enter a number:"))

if(number<0):
    print("Factorial cannot be found for negative numbers")
elif (number==0):
    print("Factorial of 0 is 1")
else:
    print("Factorial of ", number, "is: ",factorial(number))
