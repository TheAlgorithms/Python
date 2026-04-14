"""
Console-free grocery cart logic.
"""


class GroceryStoreCart:
    """
    Maintain cart item quantities and compute totals.

    >>> cart = GroceryStoreCart({"apple": 1.5, "milk": 2.0})
    >>> cart.add_item("apple", 2)
    >>> cart.add_item("milk")
    >>> round(cart.total_price(), 2)
    5.0
    >>> cart.remove_item("apple")
    >>> round(cart.total_price(), 2)
    3.5

    >>> GroceryStoreCart({})
    Traceback (most recent call last):
    ...
    ValueError: price_catalog cannot be empty

    >>> cart.add_item("bread")
    Traceback (most recent call last):
    ...
    KeyError: "'bread' is not in the catalog"

    >>> cart.add_item("apple", 0)
    Traceback (most recent call last):
    ...
    ValueError: quantity must be positive

    >>> cart.remove_item("milk", 0)
    Traceback (most recent call last):
    ...
    ValueError: quantity must be positive

    >>> empty_cart = GroceryStoreCart({"apple": 1.5})
    >>> empty_cart.remove_item("apple")
    Traceback (most recent call last):
    ...
    KeyError: "'apple' is not present in the cart"

    >>> GroceryStoreCart({})
    Traceback (most recent call last):
    ...
    ValueError: price_catalog cannot be empty

    >>> cart.add_item("bread")
    Traceback (most recent call last):
    ...
    KeyError: "'bread' is not in the catalog"

    >>> cart.add_item("apple", 0)
    Traceback (most recent call last):
    ...
    ValueError: quantity must be positive

    >>> cart.remove_item("milk", 0)
    Traceback (most recent call last):
    ...
    ValueError: quantity must be positive

    >>> empty_cart = GroceryStoreCart({"apple": 1.5})
    >>> empty_cart.remove_item("apple")
    Traceback (most recent call last):
    ...
    KeyError: "'apple' is not present in the cart"
    """

    def __init__(self, price_catalog: dict[str, float]) -> None:
        if not price_catalog:
            raise ValueError("price_catalog cannot be empty")
        self.price_catalog = dict(price_catalog)
        self.quantities: dict[str, int] = {}

    def add_item(self, item: str, quantity: int = 1) -> None:
        if item not in self.price_catalog:
            msg = f"{item!r} is not in the catalog"
            raise KeyError(msg)
        if quantity <= 0:
            raise ValueError("quantity must be positive")
        self.quantities[item] = self.quantities.get(item, 0) + quantity

    def remove_item(self, item: str, quantity: int = 1) -> None:
        if quantity <= 0:
            raise ValueError("quantity must be positive")
        current = self.quantities.get(item, 0)
        if current == 0:
            msg = f"{item!r} is not present in the cart"
            raise KeyError(msg)
        if quantity > current:
            raise ValueError("quantity exceeds amount present in the cart")
        if quantity > current:
            raise ValueError("quantity exceeds amount present in the cart")
        if quantity == current:
            self.quantities.pop(item, None)
        else:
            self.quantities[item] = current - quantity

    def total_price(self) -> float:
        return sum(
            self.price_catalog[item] * qty for item, qty in self.quantities.items()
        )


if __name__ == "__main__":
    import doctest

    doctest.testmod()
