class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return "Deposit successful"
        else:
            return "Invalid deposit amount"
    def withdraw(self, amount):
        if amount <= 0:
            return "Invalid withdrawal amount"
        elif amount > self.__balance:
            return "Insufficient balance"
        else:
            self.__balance -= amount
            return "Withdrawal successful"
    def get_balance(self):
        return self.__balance

account = BankAccount(0)
print(f"{account.deposit(500)},now your balance is:  {account.get_balance()}")
print(f"{account.withdraw(300)}, now your balance is: {account.get_balance()}")
print(f"{account.withdraw(100)},now your balance is: {account.get_balance()}")
print(f"{account.withdraw(200)},now your balance is: {account.get_balance()}")

