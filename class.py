class BankAccount:

    def __init__(self, name, money):
        self.name = name
        self.balance = money

    def deposit(self, money):
        self.balance += money
        print(f"You have just deposited : {money}")

    def withdraw(self, money):
        if self.balance > money:
            self.balance -= money
            print("You have Withdraw :", money)
        else:
            return "Insufficient funds"

    def checkbalance(self):
        print(f"Your balance is : {self.balance}")


sheriff = BankAccount('sheriff', 1000)
sheriff.withdraw(300)
sheriff.deposit(100)
sheriff.checkbalance()
