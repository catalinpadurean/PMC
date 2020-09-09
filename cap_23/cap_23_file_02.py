""" Creating a bank account object """

class Account: #Class
    """This is the main class"""
    
    def __init__(self, filepath): #Constructor
        self.filepath = filepath  #Instance variable
        with open(self.filepath, 'r') as balance_file: #balance_file is a temporary variable where the file is stored
            self.balance = int(balance_file.read()) #read as a string by default and covert to integer
    
    def withdraw(self, amount): #Class method
        self.balance = self.balance - amount
        
    def deposit(self, amount):
        self.balance = self.balance + amount

    def commit(self ):
        with open(self.filepath, 'w') as balance_file: #balance_file is a temporary variable where the file is stored
            balance_file.write(str(self.balance))

""" Understanding Inheritace"""  
#Inheritance is the process of creating a new class out of the base class that will have all the properties and methods of the base class but also it's own
#Data members are instance and class variables

class Checking(Account):
    """This is the inherited class"""
    
    type = "checking" #Class variable. Shared by all instances of the class. Declared outside of class functions
    
    def __init__(self, filepath, fee):
        self.fee = fee
        Account.__init__(self, filepath)
    
    def transfer (self, amount ):
        self.balance = self.balance - amount - self.fee
        

"""Test code"""

my_acc = Account("balance.txt")  #Object Instance
print(my_acc.balance) 
my_acc.withdraw(50)
print(my_acc.balance)
my_acc.commit()
my_acc.deposit(10)
print(my_acc.balance)
my_acc.commit() 

print(my_acc.__doc__) #Doc String printed

myCheckAcc = Checking("balance.txt",1)
myCheckAcc.deposit(10)
print(myCheckAcc.balance)
myCheckAcc.withdraw(100)
print(myCheckAcc.balance)
myCheckAcc.transfer(8)
print(myCheckAcc.balance)
myCheckAcc.commit()
print("My account type")
print(myCheckAcc.type)


yourCheckAcc = Checking ("balance_.txt", 2)
yourCheckAcc.deposit(10)
print(yourCheckAcc.balance)
yourCheckAcc.withdraw(100)
print(yourCheckAcc.balance)
yourCheckAcc.transfer(8)
print(yourCheckAcc.balance)
yourCheckAcc.commit()
print("Your account type")
print(myCheckAcc.type)