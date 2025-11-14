class Account():

    #constructor
    def __init__(self, owner, balance = 0):
        self.owner = owner
        self.balance = balance

    #str method
    def __str__(self):
        return f'Account owner:   {self.owner}\nAccount balance: ${self.balance}'
    
    #deposit method
    def deposit(self, deposit_amt):
        if deposit_amt > 0:
            self.balance += deposit_amt
            print(f'You have successfully deposited ${deposit_amt}!')
        else:
            print("Sorry, you cannot deposit zero or negative amount")

    #withdraw
    def withdraw(self, withdraw_amt):
        if withdraw_amt <= self.balance:
            self.balance -= withdraw_amt
            print(f'Withdrawal accepted')
        else:
            print('Funds Unavailable!')
    
myAccount = Account('Long Ngo', 1000)
print(myAccount)
print(myAccount.owner)
print(myAccount.balance)

print('=========== test deposit ===========')
myAccount.deposit(0)
myAccount.deposit(-2)
myAccount.deposit(50)
print(f'current amount: {myAccount.balance}') #1050

print('=========== test withdraw ===========')
myAccount.withdraw(5000)
myAccount.withdraw(200) 
print(f'current amount after withdraw: {myAccount.balance}')  #850

myAccount.withdraw(850)
print(f'current amount after withdraw: {myAccount.balance}')  #0
