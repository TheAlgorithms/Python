def compress(value):
    if value not in coordinate_map:
        raise ValueError(f"{value} not found in coordinate map")
    return coordinate_map[value]


def decompress(index):
    if index < 0 or index >= len(original_values):
        raise ValueError(f"Index {index} is out of bounds")
    return original_values[index]
