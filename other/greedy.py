class Things:
    def __init__(self, name, value, weight):
        self.name = name
        self.value = value
        self.weight = weight

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, {self.value}, {self.weight})"

    def get_value(self):
        return self.value

    def get_name(self):
        return self.name

    def get_weight(self):
        return self.weight

    def value_weight(self):
        return self.value / self.weight


def build_menu(name, value, weight):
    menu = []
    for i in range(len(value)):
        menu.append(Things(name[i], value[i], weight[i]))
    return menu


def greedy(item, max_cost, key_func):
    items_copy = sorted(item, key=key_func, reverse=True)
    result = []
    total_value, total_cost = 0.0, 0.0
    for i in range(len(items_copy)):
        if (total_cost + items_copy[i].get_weight()) <= max_cost:
            result.append(items_copy[i])
            total_cost += items_copy[i].get_weight()
            total_value += items_copy[i].get_value()
    return (result, total_value)


def test_greedy():
    """
    >>> food = ["Burger", "Pizza", "Coca Cola", "Rice",
    ...         "Sambhar", "Chicken", "Fries", "Milk"]
    >>> value = [80, 100, 60, 70, 50, 110, 90, 60]
    >>> weight = [40, 60, 40, 70, 100, 85, 55, 70]
    >>> foods = build_menu(food, value, weight)
    >>> foods  # doctest: +NORMALIZE_WHITESPACE
    [Things(Burger, 80, 40), Things(Pizza, 100, 60), Things(Coca Cola, 60, 40),
     Things(Rice, 70, 70), Things(Sambhar, 50, 100), Things(Chicken, 110, 85),
     Things(Fries, 90, 55), Things(Milk, 60, 70)]
    >>> greedy(foods, 500, Things.get_value)  # doctest: +NORMALIZE_WHITESPACE
    ([Things(Chicken, 110, 85), Things(Pizza, 100, 60), Things(Fries, 90, 55),
      Things(Burger, 80, 40), Things(Rice, 70, 70), Things(Coca Cola, 60, 40),
      Things(Milk, 60, 70)], 570.0)
    """


if __name__ == "__main__":
    import doctest

    doctest.testmod()
