# Define the structure of a node in the linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Define the singly linked list class
class SinglyLinkedList:
    def __init__(self):
        self.head = None

    # Function to insert a node at the beginning of the list
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Function to insert a node at the end of the list
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    # Function to insert a node at a specified position (middle)
    def insert_at_middle(self, data, position):
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
    def delete_at_beginning(self):
        if not self.head:
            print("List is empty. Nothing to delete.")
            return
        self.head = self.head.next

    # Function to delete a node at the end of the list
    def delete_at_end(self):
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
    def delete_at_middle(self, position):
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
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# Main program
if __name__ == "__main__":
    linked_list = SinglyLinkedList()

    while True:
        print("\nLinked List Operations:")
        print("1. Insert at Beginning")
        print("2. Insert at End")
        print("3. Insert at Middle")
        print("4. Delete at Beginning")
        print("5. Delete at End")
        print("6. Delete at Middle")
        print("7. Display")
        print("8. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            data = int(input("Enter data to insert at the beginning: "))
            linked_list.insert_at_beginning(data)
            linked_list.display()
        elif choice == 2:
            data = int(input("Enter data to insert at the end: "))
            linked_list.insert_at_end(data)
            linked_list.display()
        elif choice == 3:
            data = int(input("Enter data to insert: "))
            position = int(input("Enter position to insert: "))
            linked_list.insert_at_middle(data, position)
            linked_list.display()
        elif choice == 4:
            linked_list.delete_at_beginning()
            linked_list.display()
        elif choice == 5:
            linked_list.delete_at_end()
            linked_list.display()
        elif choice == 6:
            position = int(input("Enter position to delete: "))
            linked_list.delete_at_middle(position)
            linked_list.display()
        elif choice == 7:
            linked_list.display()
        elif choice == 8:
            break
        else:
            print("Invalid choice. Please try again.")
