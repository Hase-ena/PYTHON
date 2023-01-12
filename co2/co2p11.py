'''area of square'''
area=lambda x:x*x
side=int(input("enter the side of the square:"))
print("area=",area(side))
print("\n")
'''area of rectangle'''
area=lambda x,y:x*y
a=int(input("enter the length of the rectangle:"))
b=int(input("enter the breadth of the rectangle:"))
print("area=",area(a,b))
print("\n")
'''area of triangle'''
area=lambda p,q:0.5*(p*q)
p=int(input("enter the height of the triangle:"))
q=int(input("enter the breadth of the triangle:"))
print("area=",area(p,q))