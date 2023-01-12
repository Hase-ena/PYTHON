'''class encap:
    __a=10
    def __display(self):
        print("welcome")
        print("instance variable",self.__a)
    def show(self):
        #self.__display
        print("mca")
        print(self.__display())
obj=encap()
#print(self.__a)
#obj.display()
obj.show()'''


class encap:
    __a=10
    def display(self):
        print("welcome",self.__a)
obj=encap()
obj.display()