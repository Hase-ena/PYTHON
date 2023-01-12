class bank:
    def __init__(self):
        self.accountno=int(input("Enter the account number"))
        self.name=input("Enter the name")
        self.type=input("Enter the type of account  s/c")
        self.balance=0
    def deposit(self):
        self.deposit=int(input("Enter the amount to be deposit"))
        self.balance=self.balance+self.deposit
        return self.balance
    def withdraw(self):
        self.withdraw=int(input("Enter the amount to withdraw"))
        if(self.balance<self.withdraw):
            print("No sufficient balance to withdraw")
        else:
            self.balance=self.balance-self.withdraw
            return self.balance
    def display(self):
        print("Net Balance:",self.balance)
a=bank()
while(True):
    print("\n 1.Deposit \n 2.Withdraw \n 3.Balance \n 4.Exit")
    option=int(input("Enter the choice"))
    if(option==1):
        a.deposit()
        a.display()
    elif(option==2):
        a.withdraw()
        a.display()
    elif(option==3):
        a.display()
    else:
        exit(0)
a.display()       
b=bank()
b.deposit()
b.withdraw()