from graphics.rectangle import*
from graphics.circle import*
from graphics.rectangle import*
from graphics.threeDgraphics.cuboid import*
from graphics.threeDgraphics.sphere import*

l=int(input("enter the lenghth of the rectangle:"))
b=int(input("enter the breadth of the rectangle:"))
print("perimeter of the rectangle=",rectPerimeter(l,b))
print("area of the rectangle=",rectArea(l,b))
print()

r=int(input("enter the radius of the circle:"))
print("perimeter of the circle=",circlePerimeter(r))
print("area of the circle=",circleArea(r))
print()

l1=int(input("enter the lenghth of the cuboid:"))
b1=int(input("enter the breadth of the cuboid:"))
h1=int(input("enter the height of the cuboid:"))
print("perimeter of the cuboid=",perimeter(l1,b1,h1))
print("area of the cuboid=",area(l1,b1,h1))
print()

r1=int(input("enter the radius of the sphere:"))
print("perimeter of the sphere=",SpPerimeter(r1))
print("area of the sphere=",SpArea(r1))
print()