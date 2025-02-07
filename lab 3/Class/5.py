class Account:
    def __init__(self,owner,balance):
        self.owner = owner
        self.balance = float(balance)
    def deposit(self,amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount} New Balance: ${self.balance} ") 
        else:
            print("Amount must be greater than 0")
    def withdraw(self,amount):
        if amount > self.balance:
            print(f"❌ Insufficient funds! Available balance: ${self.balance:.2f}")
        elif amount <= 0:
            print("Amount must be greater than 0")
        else:
            self.balance -= amount
            print(f"Withdrawn ${amount} New Balance: ${self.balance}")

    def show_balance(self):
        print(f"{self.owner}'s Accaunt Balance: ${self.balance}")

owner,balance = input().split()
balance = float(balance)
account = Account(owner,balance)

account.show_balance()

amount = int(input())

account.deposit(amount)
account.withdraw(amount)
account.withdraw(amount)

account.show_balance()