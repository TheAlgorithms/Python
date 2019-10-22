class Node:  # create a Node
    def __init__(self, data):
        self.data = data  # given data
        self.next = None  # given next to None


class Linked_List:
    def __init__(self):
        self.head = None  # Initialize head to None

    def insert_tail(self, data):
        if self.head is None:
            self.insert_head(data)  # If this is first node, call insert_head
        else:
            temp = self.head
            while temp.next != None:  # traverse to last node
                temp = temp.next
            temp.next = Node(data)  # create node & link to tail

    def insert_head(self, data):
        newNod = Node(data)  # create a new node
        if self.head != None:
            newNod.next = self.head  # link newNode to head
        self.head = newNod  # make NewNode as head

    def printList(self):  # print every node data
        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.next

    def delete_head(self):  # delete from head
        temp = self.head
        if self.head != None:
            self.head = self.head.next
            temp.next = None
        return temp

    def delete_tail(self):  # delete from tail
        temp = self.head
        if self.head != None:
            if self.head.next is None:  # if head is the only Node in the Linked List
                self.head = None
            else:
                while temp.next.next is not None:  # find the 2nd last element
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


def main():
    A = Linked_List()
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


if __name__ == "__main__":
    main()
