class BankAccount:
    def __init__(self, initial_balance=0):
        """Initialize the bank account with an optional initial balance (default: 0)."""
        self.__account_balance = initial_balance   # private attribute

    def deposit(self, amount):
        """Deposit a positive amount into the account."""
        if amount > 0:
            self.__account_balance += amount
            return True
        return False

    def withdraw(self, amount):
        """Withdraw amount if sufficient funds exist. Returns True if successful, else False."""
        if 0 < amount <= self.__account_balance:
            self.__account_balance -= amount
            return True
        return False

    def display_balance(self):
        """Return the current account balance as a formatted string."""
        return f"Current Balance: ${self.__account_balance}"
