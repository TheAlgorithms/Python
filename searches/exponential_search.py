from binary_search import binary_search


def exponential_search(sorted_collection: list[int], item: int) -> int | None:
    bound = 1
    while bound < len(sorted_collection) and sorted_collection[bound] < item:
        bound *= 2
    if bound < len(sorted_collection) and sorted_collection[bound] == item:
        return bound
    last_bound = bound / 2
    sorted_collection = sorted_collection[int(last_bound) : bound + 1]
    index_in_optimized_list = binary_search(
        sorted_collection=sorted_collection, item=item
    )
    if index_in_optimized_list is None:
        return None
    return int(index_in_optimized_list) + int(bound / 2)
