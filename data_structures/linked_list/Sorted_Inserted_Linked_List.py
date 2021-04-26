class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Circular_Linked_List:
    def __init__(self):
        self.head = None

    def Sorted_Insert(self, new_node):
        current = self.head
        if current is None:
            new_node.next = new_node
            self.head = new_node
        elif current.data >= new_node.data:
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head
            self.head = new_node
        else:
            while current.next != self.head and current.next.data < new_node.data:
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def Display(self):
        temp = self.head
        if self.head is not None:
            while(temp):
                print(temp.data, "->", end=" ")
                temp = temp.next
                if temp == self.head:
                    print(temp.data)
                    break


if __name__ == "__main__":
    L_list = Circular_Linked_List()
    Test_list = [12, 56, 2, 11, 1, 90]
    for keys in Test_list:
        temp = Node(keys)
        L_list.Sorted_Insert(temp)
    print("Sorted Inserted Circular Linked List: ")
    L_list.Display()
