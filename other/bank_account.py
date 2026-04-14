"""
Simple BankAccount class demonstrating core OOP concepts.

Reference:
Invariant-preserving bank account state model.

This module implements a minimal transactional data model whose computational
value is the enforcement of account invariants during constant-time state
transitions: account identifiers must be present, balances may not start
negative, deposits must be positive, and withdrawals may not overdraw the
account.
"""


class BankAccount:
    """
    Stateful account abstraction with validated balance updates.

    The class is intentionally small, but its purpose is not to serve as a
    generic OOP tutorial. It provides a compact example of how to model a
    mutable record while preserving correctness constraints across operations,
    with each transaction executing in O(1) time.
    >>> account = BankAccount("ACC-1001", initial_balance=100.0)
    >>> account.balance
    100.0
    >>> account.deposit(50)
    150.0
    >>> account.withdraw(20)
    130.0
    >>> account.account_number
    'ACC-1001'

    >>> BankAccount("", initial_balance=10.0)
    Traceback (most recent call last):
    ...
    ValueError: account_number must be provided

    >>> BankAccount("ACC-1002", initial_balance=-1.0)
    Traceback (most recent call last):
    ...
    ValueError: initial_balance cannot be negative

    >>> account.deposit(0)
    Traceback (most recent call last):
    ...
    ValueError: deposit amount must be positive

    >>> account.withdraw(0)
    Traceback (most recent call last):
    ...
    ValueError: withdraw amount must be positive

    >>> account.withdraw(1000)
    Traceback (most recent call last):
    ...
    ValueError: insufficient funds
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
