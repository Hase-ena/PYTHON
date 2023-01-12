class time:
    def __init__(self):
        self.hour=int(input("enter the hour:"))
        self.minute=int(input("enter the minute:"))
        self.seconds=int(input("enter the seconds:"))
    def __add__(self,t):
        hr=self.__hr +t.__hr
        print("Sum of hours:",hr)
        mi = self.__min +t.__min
        print("Sum of minutes:",mi)
        sec = self.__sec +t.__sec
        print("Sum of seconds:",sec)
          
        if mi>=60:
            hr=hr+ 1
            mi=mi-60
        if sec >=60:
            mi=mi+1
            sec=sec-60
        return hr,mi,sec
t1 = time()
t2 = time()
print("hour,min,sec",t1+t2)