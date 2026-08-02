class BankAccount:
    def __init__(self, account_number, balance, date_of_opening, customer_name):
        self.account_number = account_number
        self.balance = balance
        self.date_of_opening = date_of_opening
        self.customer_name = customer_name

    def deposit(self):
        amount = int(input("Enter deposit amount: "))
        if amount > 0:
            self.balance += amount
            print(f"Successfully deposited {amount}. Current balance: {self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self):
        amount = int(input("Enter withdrawal amount: "))
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Successfully withdrew {amount}. Remaining balance: {self.balance}")
        else:
            print("Insufficient balance or invalid amount.")

    def check_balance(self):
        print(f"Current Balance for {self.customer_name}: {self.balance}")
        return self.balance


acc1 = BankAccount("854976", 50000, "20 July, 2026", "Shadat Ahmed")
acc1.check_balance()
acc1.deposit()
acc1.withdraw()