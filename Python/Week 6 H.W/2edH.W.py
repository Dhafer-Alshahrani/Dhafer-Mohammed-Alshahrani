class BankAccount:
    '''
    THIS IS A SEMI BANK MECHAIN THAT ALLOWS PEOPLE TO DEAK WITH THIER MONEY EASILY
    self.owner in this code : is stands for the owner of the objects that i will creat as many as i want .'''
    CURRENCY = "SAR"
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        self.amount = amount
        if self.amount == 0:
            return f" you can not add Zero to the balance"
        if self.amount < 0:
            return f" you can not deak with negative number "
        self.balance +=amount
        return f"This is now your balance: \n{self.balance}"
    def withdraw(self, amount):
        self.amount = amount
        if self.amount == 0:
            return f" you can not take a  Zero from the balance"
        if self.amount < 0:
            return f" you can not deak with negative number "
        self.balance -=amount
        return f" This is now your balance: \n {self.balance}"

    def show_balance(self):
        return f" {self.owner} has a balance of : \n {self.balance} {self.CURRENCY}"
dha = BankAccount("Dhafer",2000)
print(dha.deposit(200))
print(dha.withdraw(100))
print(dha.show_balance())
# #help(dha) IT's optional to check it 
