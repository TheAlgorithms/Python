class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_node(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def remove_node(self, data):
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# Main program
linked_list = LinkedList()

while True:
    print("\nOptions:")
    print("1. Insert a node")
    print("2. Remove a node")
    print("3. Reverse the linked list")
    print("4. Print the linked list")
    print("5. Exit")
    
    choice = input("Enter your choice: ")

    if choice == '1':
        data = input("Enter data to insert: ")
        linked_list.insert_node(data)
    elif choice == '2':
        data = input("Enter data to remove: ")
        linked_list.remove_node(data)
    elif choice == '3':
        linked_list.reverse()
    elif choice == '4':
        print("Linked List:")
        linked_list.display()
    elif choice == '5':
        break
    else:
        print("Invalid choice. Please try again.")
