class Account:
    def __init__(self,ID = 0, balance = 100, annualInterestRate = 0):
        self.ID = ID
        self.balance = balance
        self.annualInterestRate = annualInterestRate

    def getID(self):
        return self.ID

    def setID(self, ID):
        self.ID = ID

    def setBalance(self,balance):
        self.balance = balance

    def getBalance(self):
        return self.balance

    def getAnnualInterestRate(self):
        return self.annualInterestRate

    def setAnnualInterestRate(self, annualInterestRate):
        self.annualInterestRate = annualInterestRate

    def getMonthlyInterest(self):
        return self.balance * self.getMonthlyInterestRate()

    def getMonthlyInterestRate(self):
        return (self.annualInterestRate / 100) / 12

    def withdraw(self, amount):
        self.balance = self.balance - amount

    def deposit(self, amount):
        self.balance = self.balance + amount

