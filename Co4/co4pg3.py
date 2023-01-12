class rectangle:
    def __init__(self):
        self.__l=int(input("Enter the length of rectangle:"))
        self.__b=int(input("Enter the breadth of rectangle:"))
    def __lt__(self,obj2):
        a1 = self.__l * self.__b
        a2 = obj2.__l * obj2.__b
        print("Area of 1st rectangle:",a1)
        print("Area of 2nd rectangle:",a2)
        return a1<a2
obj1 = rectangle()
obj2 = rectangle()
if obj1<obj2:
    print("obj 1 is lessthan obj2")
else:
    print("obj1 is greaterthan or equalto obj2")