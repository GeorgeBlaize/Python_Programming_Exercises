
# Python Program to Print the Fibonacci sequence

nterms = int(input("How many terms? "))

n1,n2=0,1
cout = 0

if nterms<=0:
    print("Please enter a positive integer")
elif nterms==1:
    print("Fibonacci sequence upto",nterms,":")
    print(n1)
else:
    print("Fibonacci sequence: ")
    while cout<nterms:
        print(n1)
        nth=n1+n2
        n1=n2
        n2=nth
        cout+=1
