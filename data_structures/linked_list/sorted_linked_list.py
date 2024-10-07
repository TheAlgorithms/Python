class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SortedLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        # Case when the list is empty or the new node needs to be at the head
        if self.head is None or self.head.data >= new_node.data:
            new_node.next = self.head
            self.head = new_node
        else:
            # Find the correct position to insert the new node
            current = self.head
            while current.next is not None and current.next.data < new_node.data:
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# Create an instance of SortedLinkedList
sll = SortedLinkedList()
# Take input from the user
while True:
    try:
        user_input = input("Enter a number (or 'q' to quit): ")
        if user_input == "q":
            break
        else:
            num = int(user_input)
            sll.insert(num)
    except ValueError:
        print("Please enter a valid number or 'q' to quit.")
# Display the sorted linked list
print("Sorted Linked List:")
sll.display()
