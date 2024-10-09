from typing import Any, List

def bubble_sort_iterative(collection: List[Any]) -> List[Any]:
    """Sorts a collection using the iterative bubble sort algorithm.

    :param collection: A mutable ordered collection with comparable items.
    :return: The same collection ordered in ascending order.
    """
    length = len(collection)
    for i in range(length):
        swapped = False
        for j in range(length - 1 - i):
            if collection[j] > collection[j + 1]:
                swapped = True
                collection[j], collection[j + 1] = collection[j + 1], collection[j]
        if not swapped:
            break  # Stop iteration if the collection is sorted.
    return collection


def bubble_sort_recursive(collection: List[Any]) -> List[Any]:
    """Sorts a collection using the recursive bubble sort algorithm.

    :param collection: A mutable ordered sequence of elements.
    :return: The same list in ascending order.
    """
    if len(collection) <= 1:
        return collection
    
    # Perform a single pass of bubble sort
    swapped = False
    for i in range(len(collection) - 1):
        if collection[i] > collection[i + 1]:
            swapped = True
            collection[i], collection[i + 1] = collection[i + 1], collection[i]
    
    if not swapped:
        return collection
    
    return bubble_sort_recursive(collection[:-1]) + [collection[-1]]


if __name__ == "__main__":
    # Example usage
    sample_list = [5, 3, 8, 6, 2]
    print("Iterative Bubble Sort:", bubble_sort_iterative(sample_list.copy()))
    print("Recursive Bubble Sort:", bubble_sort_recursive(sample_list.copy()))
