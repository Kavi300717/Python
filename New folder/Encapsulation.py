class Pen:
    def __init__(self):
        self.__ink_level = 100

    def write(self):
        if self.__ink_level > 0:
            self.__ink_level -= 10
            print("Writing...")
        else:
            print("No ink left!!")
    
    def refill(self):
        self.__ink_level = 100
        print("Pen refilled")

    def check_ink(self):
        print(f"Ink level: {self.__ink_level}%")

# mu_pen = Pen()
# mu_pen.write()
# mu_pen.check_ink()

# mu_pen.refill()
# mu_pen.check_ink()

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposite(self, amount):
        if  amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}")
        else:
            print("Deposited amount must be positive")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdraw ${amount}")
        else:
            print("Insufficient balance or invalid amount")

    def check_balance(self):
        print(f"Current balance: ${self.__balance}")

account = BankAccount(15000)
account.check_balance()
account.deposite(1250)
account.check_balance()
account.withdraw(50)
account.check_balance()