
# Python Program to Find Sum of n Natural Numbers

number=int(input("Enter the value of n: "))
hold=number
sum=0

if number<=0:
    print("Enter a whole positive number!")

else:
    while number>0:
        sum=sum+number
        number-=1

    print("Sum of first",hold,"natural numbers is: ",sum)
