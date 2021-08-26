class Item:
    def __init__(self, name: str, weight: float, rating: float) -> None:
        self._name = name
        self._weight = weight
        self._rating = rating
        self._quantity = 0

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        self._name = name

    @property
    def weight(self) -> float:
        return self._weight

    @weight.setter
    def weight(self, weight: float) -> None:
        self._weight = weight

    @property
    def rating(self) -> float:
        return self._rating

    @rating.setter
    def rating(self, rating: float) -> None:
        self._rating = rating

    @property
    def quantity(self) -> int:
        return self._quantity

    @quantity.setter
    def quantity(self, quantity: int) -> None:
        self._quantity = quantity
