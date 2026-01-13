class Wallet:
    def __init__(self, balance):
        self.balance = balance
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
    def deposit(self, amount):
        self.balance += amount
    def __add__(self, other):
        return f"{self.balance + other.balance} bdt"
w1 = Wallet(200)
w2 = Wallet(300)
print(w1 + w2)