


class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be greater than 0.")
            return
        self.balance += amount
        print(f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be greater than 0.")
            return
        if amount > self.balance:
            print("Insufficient funds. Withdrawal canceled.")
            return
        self.balance -= amount
        print(f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}")

    def get_balance(self):
        return self.balance


account1 = BankAccount("Alice")
account2 = BankAccount("Bob", 100)


account1.deposit(50)
account1.withdraw(20)
account1.withdraw(40)  

account2.deposit(-10)  
account2.withdraw(200) 

print(f"{account1.account_holder}'s Balance: ${account1.get_balance():.2f}")
print(f"{account2.account_holder}'s Balance: ${account2.get_balance():.2f}")
