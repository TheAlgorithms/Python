class Node:
    """class to represent a node in a linked list."""
    def __init__(self, data):
        self.data = data  # store the value of the node
        self.next = None  # pointer to the next node


def array_to_linked_list(arr):
    """Convert an array to a linked list and return the head of the linked list."""
    if arr is None:  # checking if the input array is empty
        return None  # if empty it will return nothing

    head = Node(arr[0])  # create head node
    n = head  # pointer to the head node

    # loop through the array starting from the second element coz 1st element is head
    for value in arr[1:]:
        n.next = Node(value)  # creating a new node
        n = n.next

    return head


def print_linked_list(head):
    """printing the linked list."""
    n = head
    while n is not None:
        print(n.data, end=" -> " if n.next else "")
        n = n.next
    print(" -> Null")  # for a new line at end which will also add -> null at end


# main function to take user input
def main():
    user_input = input("Enter a list of integers separated by spaces: ")

    arr = list(map(int, user_input.split()))  # convert input string to a list of integers

    linked_list_head = array_to_linked_list(arr)

    print("Linked List: ", end="")
    print_linked_list(linked_list_head)


if __name__ == "__main__":
    main()
