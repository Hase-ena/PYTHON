y=int(input("enter the current year:"))
x=int(input("enter the final year:"))
print("leap years are:")
if y<x:
    for i in range (y,x):
        if i%4==0 and i%100!=0:
            print(i)
        else:
            i +=1
else:
    print("no leap year")