from binary_search import binary_search_by_recursion


def exponential_search(sorted_collection: list[int], item: int) -> int | None:
    bound = 1
    while bound < len(sorted_collection) and sorted_collection[bound] < item:
        bound *= 2
    left = bound / 2
    right = min(bound, len(sorted_collection) - 1)
    return binary_search_by_recursion(
        sorted_collection=sorted_collection, item=item, left=left, right=right
    )
