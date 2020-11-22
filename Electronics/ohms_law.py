# Defining function
def ohms_law(v: float = 0, i: float = 0, r: float = 0) -> float:
    if v == 0:
        result = i * r
        return result
    elif i == 0:
        result = v / r
        return result
    elif r == 0:
        result = v / i
        return result
    else:
        return 0
