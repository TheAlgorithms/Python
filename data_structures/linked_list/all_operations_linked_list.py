# Define the structure of a node in the linked list
class Node:
    def __init__(self, data) -> None:
        """
        Initialize a new node with the given data.

        :param data: Data to be stored in the node.
        :type data: int
        """
        self.data = data
        self.next = None

# Define the singly linked list class
class SinglyLinkedList:

    def __init__(self) -> None:
        """
        Initialize an empty singly linked list.
        """
        self.head = None

    # Function to insert a node at the beginning of the list
    def insert_at_beginning(self, data) -> None:
        """
        :param data: Data to be inserted.
        :type data: int
        """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Function to insert a node at the end of the list
    def insert_at_end(self, data) -> None:
        """
        :param data: Data to be inserted.
        :type data: int
        """
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    # Function to insert a node at a specified position (middle)
    def insert_at_middle(self, data, position) -> None:
        """
        Insert a new node at the specified position in the linked list.

        :param data: Data to be inserted.
        :type data: int
        :param position: Position at which the data should be inserted.
        :type position: int
        :raise ValueError: If the position is invalid.
        """
        if position <= 0:
            print("Invalid position.")
            return
        if position == 1:
            self.insert_at_beginning(data)
            return
        new_node = Node(data)
        current = self.head
        count = 1
        while count < position - 1 and current.next:
            current = current.next
            count += 1
        if count != position - 1:
            print("Position out of range.")
            return
        new_node.next = current.next
        current.next = new_node

    # Function to delete a node at the beginning of the list
    def delete_at_beginning(self) -> None:
        """
        :raise ValueError: If the list is empty.
        """
        if not self.head:
            print("List is empty. Nothing to delete.")
            return
        self.head = self.head.next

    # Function to delete a node at the end of the list
    def delete_at_end(self) -> None:
        """
        :raise ValueError: If the list is empty.
        """
        if not self.head:
            print("List is empty. Nothing to delete.")
            return
        if not self.head.next:
            self.head = None
            return
        current = self.head
        while current.next.next:
            current = current.next
        current.next = None

    # Function to delete a node at a specified position (middle)
    def delete_at_middle(self, position) -> None:
        """
        :param position: Position of the node to be deleted.
        :type position: int
        :raise ValueError: If the position is invalid.
        """
        if position <= 0:
            print("Invalid position.")
            return
        if position == 1:
            self.delete_at_beginning()
            return
        current = self.head
        count = 1
        while count < position - 1 and current.next:
            current = current.next
            count += 1
        if count != position - 1 or not current.next:
            print("Position out of range.")
            return
        current.next = current.next.next

    # Function to display the linked list
    def display(self) -> None:
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Main program
if __name__ == "__main__":
    linked_list = SinglyLinkedList()

    # Insert nodes
    linked_list.insert_at_beginning(10)
    print(linked_list.display())
    """
    >>> linked_list.display()
    '10 -> None'
    """

    linked_list.insert_at_end(20)
    print(linked_list.display())
    """
    >>> linked_list.display()
    10 -> 20 -> None
    """

    linked_list.insert_at_middle(15, 2)
    print(linked_list.display())
    """
    >>> linked_list.display()
    '10 -> 15 -> 20 -> None
    """

    # Delete nodes
    linked_list.delete_at_beginning()
    print(linked_list.display())
    """
    >>> linked_list.display()
    15 -> 20 -> None
    """

    linked_list.delete_at_end()
    print(linked_list.display())
    """
    >>> linked_list.display()
    15 -> None
    """

    linked_list.delete_at_middle(1)
    print(linked_list.display())
    """
    >>> linked_list.display()
    None
    """
