class Node:
    """A node in a singly linked list."""

    def __init__(self, data: int = 0):
        self.data = data  # The value of the node
        self.next = None  # Pointer to the next node


def array_to_linked_list(arr: list[int]) -> Node:
    """
    Convert an array into a linked list.

    :param arr: List of integers to convert into a linked list.
    :return: The head of the linked list.

    >>> array_to_linked_list([1, 2, 3])
    Node(data=1, next=Node(data=2, next=Node(data=3, next=None)))
    >>> array_to_linked_list([])
    >>> array_to_linked_list([4, 5, 6])
    Node(data=4, next=Node(data=5, next=Node(data=6, next=None)))
    """
    if arr is None:  # Check for empty array
        return None

    # Create the head of the linked list
    head = Node(arr[0])
    n = head  # Pointer to the current node

    # Loop through the array and construct the linked list
    for data in arr[1:]:
        n.next = Node(data)  # Create a new node and link it
        n = n.next  # Move to the next node

    return head  # Return the head of the linked list


# Example usage
if __name__ == "__main__":
    # Input: a list of integers
    input_array = list(map(int, input("Enter array elements separated by space: ").strip().split()))
    linked_list_head = array_to_linked_list(input_array)


    # Function to print the linked list for demonstration
    def print_linked_list(head: Node):
        """Print the linked list."""
        n = head
        while n is not None:
            print(n.data, end=" -> ")
            n = n.next
        print("None")


    # Print the resulting linked list
    print_linked_list(linked_list_head)
