import calculator
a=int(input("enter the first number:"))
b=int(input("enter the second number:"))
choice=int(input("enter your choice:"))
if(choice==1):
    s1=calculator.sum(a,b)
    print(s1)
elif(choice==2):
    s2=calculator.difference(a,b)
    print(s2)
elif(choice==3):
    s3=calculator.product(a,b)
    print(s3)
else:
    s4=calculator.division(a,b)
    print(s4)