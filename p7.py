class InsufficientFundsError(Exception):
    pass


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Deposit amount cannot be negative")
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(
                f"Cannot withdraw {amount}, balance is {self.balance}"
            )
        if amount < 0:
            raise ValueError("Withdrawal amount cannot be negative")
        self.balance -= amount


account = BankAccount("Student", 1000)
account.deposit(500)
account.withdraw(300)
print(account.balance)

try:
    account.withdraw(5000)
except InsufficientFundsError as error:
    print(f"Error: {error}")
