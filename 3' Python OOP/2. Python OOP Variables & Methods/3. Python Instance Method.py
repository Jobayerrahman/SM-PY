'''
✅ What is an Instance Method?

- An instance method is a function defined inside a class that works with instance variables (data unique to each object).

    -- It always takes 'self' as the first parameter.

    -- It can access both instance variables and class variables.

    -- It is the most common type of method used in classes.

'''


class BankAccount:
    # Constructor - initializes instance variables
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder  # instance variable
        self.balance = balance  # instance variable

    # Instance Method
    def deposit(self, amount):
        self.balance += amount
        print(f"{amount} deposited. New balance is {self.balance}")

    # Another Instance Method
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{amount} withdrawn. Remaining balance is {self.balance}")
        else:
            print("Insufficient balance!")

    # Instance Method to display account info
    def display_info(self):
        print(f"Account Holder: {self.account_holder}, Balance: {self.balance}")


# Creating objects
account1 = BankAccount("John", 5000)
account2 = BankAccount("Alice", 3000)

account1.deposit(1500)
account2.withdraw(500)
account1.display_info()
account2.display_info()

