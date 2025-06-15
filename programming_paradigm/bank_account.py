import sys
class BankAccount:
    def __init__(self, amount=0):
        self.amount = amount

    def deposit(self, amount):
        self.amount += amount

    def withdraw(self, amount):
        if amount > self.amount:
            return False
        else:
            self.amount -= amount
            return True

    def display_balance(self):
        print(f"Current Balance: ${float(self.amount)}")

