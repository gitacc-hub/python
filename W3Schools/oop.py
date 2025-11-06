# Parent class
class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance
        print(f"Account created for {self.account_holder}")
        print(f"Bank balance:{self.balance}")

    def deposit(self, amount):
        self.balance+=amount
        print(f"Deposit: {amount}")
    def withdraw(self, amount):
        if amount<=self.balance:
            self.balance-=amount
            print(f"Withdrew: {amount}")
        else:
            print("Insufficient funds")

    def display_balance(self):
        print(f"{self.account_holder} has a balance of {self.balance}")


# Child class
class SavingsAccount(BankAccount):
    def __init__(self, account_holder, balance, interest_rate):
        super().__init__(account_holder, balance)
        self.interest_rate=interest_rate

        
    def add_interest(self):
        interest=self.balance*self.interest_rate
        self.balance+=interest
        print("Interest Added")





acc2 = SavingsAccount("Bob", 2000, 0.05)
acc2.deposit(1000)
acc2.add_interest()
acc2.display_balance()
