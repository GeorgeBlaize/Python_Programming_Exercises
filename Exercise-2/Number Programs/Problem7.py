
# Python Program to Add Subtract Multiply and Divide two numbers

number1=int(input("Enter first number:"))
number2=int(input("Enter second number:"))

print("Enter which operation would you like to perform?")
ch=input("Enter any of these char for specific operation +,-,*,/:")

result=0

if ch=='+':
    result=number1+number2
elif ch=='-':
    result=number1-number2
elif ch=='*':
    result=number1*number2
elif ch=='/':
    result=number1/number2
else:
    print("Input character is not recognized!")

print(number1,ch,number2,":",result)

