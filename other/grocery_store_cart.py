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
    """

    def __init__(self, price_catalog: dict[str, float]) -> None:
        if not price_catalog:
            raise ValueError("price_catalog cannot be empty")
        self.price_catalog = dict(price_catalog)
        self.quantities: dict[str, int] = {}

    def add_item(self, item: str, quantity: int = 1) -> None:
        if item not in self.price_catalog:
            raise KeyError(f"{item!r} is not in the catalog")
        if quantity <= 0:
            raise ValueError("quantity must be positive")
        self.quantities[item] = self.quantities.get(item, 0) + quantity

    def remove_item(self, item: str, quantity: int = 1) -> None:
        if quantity <= 0:
            raise ValueError("quantity must be positive")
        current = self.quantities.get(item, 0)
        if current == 0:
            raise KeyError(f"{item!r} is not present in the cart")
        remaining = current - quantity
        if remaining > 0:
            self.quantities[item] = remaining
        else:
            self.quantities.pop(item, None)

    def total_price(self) -> float:
        return sum(self.price_catalog[item] * qty for item, qty in self.quantities.items())


if __name__ == "__main__":
    import doctest

    doctest.testmod()
