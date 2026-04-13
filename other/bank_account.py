"""
Simple BankAccount class demonstrating core OOP concepts.
"""


class BankAccount:
    """
    Basic bank account model with encapsulated account number and balance.

    >>> account = BankAccount("ACC-1001", initial_balance=100.0)
    >>> account.balance
    100.0
    >>> account.deposit(50)
    150.0
    >>> account.withdraw(20)
    130.0
    >>> account.account_number
    'ACC-1001'
    """

    def __init__(self, account_number: str, initial_balance: float = 0.0) -> None:
        if not account_number:
            raise ValueError("account_number must be provided")
        if initial_balance < 0:
            raise ValueError("initial_balance cannot be negative")

        self.__account_number = account_number
        self._balance = float(initial_balance)

    @property
    def account_number(self) -> str:
        """Read-only public accessor for the encapsulated account number."""
        return self.__account_number

    @property
    def balance(self) -> float:
        """Current account balance."""
        return self._balance

    def deposit(self, amount: float) -> float:
        """Deposit a positive amount and return updated balance."""
        if amount <= 0:
            raise ValueError("deposit amount must be positive")
        self._balance += amount
        return self._balance

    def withdraw(self, amount: float) -> float:
        """Withdraw a positive amount and return updated balance."""
        if amount <= 0:
            raise ValueError("withdraw amount must be positive")
        if amount > self._balance:
            raise ValueError("insufficient funds")
        self._balance -= amount
        return self._balance


if __name__ == "__main__":
    import doctest

    doctest.testmod()
