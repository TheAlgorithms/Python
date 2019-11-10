class Node:  # create a Node
    def __init__(self, data):
        self.data = data  # given data
        self.next = None  # given next to None

    def __repr__(self):  # String Representation of a Node
        return f"<Node: {self.data}>"


class LinkedList:
    def __init__(self):
        self.head = None  # Initialize head to None

    def insert_tail(self, data):
        if self.head is None:
            self.insert_head(data)  # If this is first node, call insert_head
        else:
            temp = self.head
            while temp.next:  # traverse to last node
                temp = temp.next
            temp.next = Node(data)  # create node & link to tail

    def insert_head(self, data):
        newNod = Node(data)  # create a new node
        if self.head:
            newNod.next = self.head  # link newNode to head
        self.head = newNod  # make NewNode as head

    def printList(self):  # print every node data
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next

    def delete_head(self):  # delete from head
        temp = self.head
        if self.head:
            self.head = self.head.next
            temp.next = None
        return temp

    def delete_tail(self):  # delete from tail
        temp = self.head
        if self.head:
            if self.head.next is None:  # if head is the only Node in the Linked List
                self.head = None
            else:
                while temp.next.next:  # find the 2nd last element
                    temp = temp.next
                temp.next, temp = (
                    None,
                    temp.next,
                )  # (2nd last element).next = None and temp = last element
        return temp

    def isEmpty(self):
        return self.head is None  # Return if head is none

    def reverse(self):
        prev = None
        current = self.head

        while current:
            # Store the current node's next node.
            next_node = current.next
            # Make the current node's next point backwards
            current.next = prev
            # Make the previous node be the current node
            prev = current
            # Make the current node the next node (to progress iteration)
            current = next_node
        # Return prev in order to put the head at the end
        self.head = prev

    def __repr__(self):  # String representation/visualization of a Linked Lists
        current = self.head
        string_repr = ""
        while current:
            string_repr += f"{current} ---> "
            current = current.next
        # END represents end of the LinkedList
        string_repr += "END"
        return string_repr

    # Indexing Support. Used to get a node at particaular position
    def __getitem__(self, index):
        current = self.head

        # If LinkedList is Empty
        if current is None:
            raise IndexError("The Linked List is empty")

        # Move Forward 'index' times
        for _ in range(index):
            # If the LinkedList ends before reaching specified node
            if current.next is None:
                raise IndexError("Index out of range.")
            current = current.next
        return current

    # Used to change the data of a particular node
    def __setitem__(self, index, data):
        current = self.head
        # If list is empty
        if current is None:
            raise IndexError("The Linked List is empty")
        for i in range(index):
            if current.next is None:
                raise IndexError("Index out of range.")
            current = current.next
        current.data = data


def main():
    A = LinkedList()
    print("Inserting 1st at head")
    a1 = input()
    A.insert_head(a1)
    print("Inserting 2nd at head")
    a2 = input()
    A.insert_head(a2)
    print("\nPrint List : ")
    A.printList()
    print("\nInserting 1st at Tail")
    a3 = input()
    A.insert_tail(a3)
    print("Inserting 2nd at Tail")
    a4 = input()
    A.insert_tail(a4)
    print("\nPrint List : ")
    A.printList()
    print("\nDelete head")
    A.delete_head()
    print("Delete Tail")
    A.delete_tail()
    print("\nPrint List : ")
    A.printList()
    print("\nReverse Linked List")
    A.reverse()
    print("\nPrint List : ")
    A.printList()
    print("\nString Representation of Linked List:")
    print(A)
    print("\n Reading/Changing Node Data using Indexing:")
    print(f"Element at Position 1: {A[1]}")
    p1 = input("Enter New Value: ")
    A[1] = p1
    print("New List:")
    print(A)


if __name__ == "__main__":
    main()
