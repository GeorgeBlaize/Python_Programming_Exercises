
# Python Program to Find Largest among Three Numbers

number1=float(input("Enter 1st number: "))
number2=float(input("Enter 2nd number: "))
number3=float(input("Enter 3rd number: "))

if(number1>number2) and (number1>number3):
    largest=number1
if (number2 > number1) and (number2 > number3):
    largest = number2
else:
    largest=number3

print("The largest number among",number1,",",number2,"and",number3,"is: ",largest)
