


class BankAccount:

    def __init__(self,owner,balance = 0):
        self.owner = owner
        self.balance = balance

    def deposit(self,amount):
        self.balance += amount
        print(f"{amount} is deposited in account and the total balance is {self.balance}")

    def withdraw(self,amount):
        if self.balance < amount:
            print(f"insufficient funds. your current available balance is {self.balance}")
        else:
            self.balance -= amount
            print(f"{amount} is withdrawn . your available balance is {self.balance}")

    def get_balance(self):
        print(f"your available balance is {self.balance}")

account = BankAccount("Alekhya")
account.get_balance()
account.deposit(2000)
account.get_balance()
account.withdraw(3000)
account.withdraw(1000)
account.get_balance()


