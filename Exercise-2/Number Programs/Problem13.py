
# Python Program to Add Digits of a Number

number=int(input("Enter a number: "))
result=0
hold=number

while number>0:
    rem=number%10
    result=result+rem
    number=int(number/10)

print("Sum of all digits of",hold,"is:",result)
