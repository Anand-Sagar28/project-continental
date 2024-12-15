# Welcome to python revision using oops concepts and all
# Write a oops program using the four pillar of program

#create a class bank and using function define its functionalities and using childs create its subclass

class Bank:
    def __init__(self, acc_holdr, balance = 0):
        self.acc_holdr = acc_holdr
        self.balance  = balance

    def deposits(self,amount):
        if(amount>0):
            self.balance += amount
            print(f"{amount} is deposited. New balance = {self.balance}")

        else:
            print("deposit amount must be greater than 0")

    def withdraw(self,amount):
        if(amount > 0):
            self.balance -= amount
            print(f"{amount} is withdrawn. New balance is {self.balance}")

        else:
            print("withdrawn amount should be greater than 0")
    
    def get_balance(self):
        print(f"Current balance is {self.balance}")

    def __str__(self):
        return f"{self.acc_holdr} is having the amount {self.balance} in the account"

class Savingsaccnt(Bank):
    def __init__(self, acc_holdr, balance = 0, intr_rate = 0.02):
        super().__init__(acc_holdr,balance)
        self.intr_rate = intr_rate
    
    def applyintr(self):
        interest = self.balance * self.intr_rate
        self.balance += interest
        print(f"The interest of {self.intr_rate * 100}% rate is being added to the principal amount and the new balance is {self.balance}")
    
    def __str__(self):
        return f"Interest rate : {self.intr_rate * 100}%, Savings account : {super().__str__()}"
    
class CheckingBal(Bank):
    def __init__(self,acc_holdr,balance= 0,overdraft_limit = 1000):
        super().__init__(acc_holdr,balance)
        self.overdraft_limit = overdraft_limit
    
    def withdraw(self,amount):
        if amount>0 and (self.balance + self.overdraft_limit > amount):
            self.balanc -= amount
            print(f"The {amount} has been withdrawn. New balance - {self.balance}")

    def __str__(self):
        return f"Withdrawn amount : {self.amount}, New balance - {self.balance}, Account holder - {self.acc_holdr}"
    
rahul_bankacc = Bank("Rahul",10000)
print(rahul_bankacc)
rahul_bankacc.deposits(4000)
rahul_bankacc.withdraw(5000)
rahul_bankacc.get_balance()

savings_account = Savingsaccnt('Anand', 200000)
print(savings_account)
savings_account.deposits(50000)
savings_account.applyintr()
savings_account.withdraw(3000)
print("balance", savings_account.get_balance())

        