class Accaunt:
    def __init__(self,owner,balance = 0):
        self.owner = owner
        self.balance = float(balance)
    def deposit(self,amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount:.2f}")
        else:
            print("Deposit amount must be more than 0")
    def withdraw(self,amount):
        if amount > self.balance :
            print(f"❌ Insufficient funds! Available balance: ${self.balance:.2f}")
        elif amount <= 0:
            print("❌ Withdrawal amount must be greater than zero.")
        else:
            self.balance -= amount
            print(f"✅ Withdrawn ${amount:.2f}. New balance: ${self.balance:.2f}")
    def show_balance(self):
        print(f"{self.o