class bank:
    def __init__(self):
        self.name=str(input("enter the name:"))
        self.accountnumber=int(input("enter the account number:"))
        self.balance=0
        self.typeofaccount=str(input("enter the type of account savings/current:"))
    def deposite (self):
        deposite=int(input("enter the amount to be deposited:"))
        self.balance=self.balance+deposite
        print(self.balance)
       
    def withdraw (self):
        amount=float(input("enter the withdraw amount:"))
        if self.balance>=amount:
            self.balance=self.balance-amount
            print("\n You Withdraw:",amount)
            print("\n Net Balance",self.balance)
        else:
            print("insufficcient balance")
    def display(self):
        print("The Net Balance",self.balance)
b_aobj=bank()
while(True):
    print("\n 1.Deposite money \n 2.withdraw money\n 3.exit")
    option=int(input("enter the choice:"))
    if(option==1):
        b_aobj.deposite()
        b_aobj.display()
    elif(option==2):
        b_aobj.withdraw()
        b_aobj.display()
    else:
        exit(0)

b_aobj.display()
a=bank()
a.deposite()
a.withdraw()
a.display()
