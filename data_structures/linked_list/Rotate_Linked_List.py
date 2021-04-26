class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linked_List:
    def __init__(self):
        self.head = None

    def Insert_At_Beginning(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node

    def Rotation(self, key):
        if key == 0:
            return
        current = self.head
        count = 1
        while count < key and current is not None:
            current = current.next
            count += 1
        if current is None:
            return
        Kth_Node = current
        while current.next is not None:
            current = current.next
        current.next = self.head
        self.head = Kth_Node.next
        Kth_Node.next = None

    def Display(self):
        temp = self.head
        while(temp):
            print(temp.data, "->", end=" ")
            temp = temp.next
        print("None")


if __name__ == "__main__":
    L_list = Linked_List()
    L_list.Insert_At_Beginning(8)
    L_list.Insert_At_Beginning(5)
    L_list.Insert_At_Beginning(10)
    L_list.Insert_At_Beginning(7)
    L_list.Insert_At_Beginning(6)
    L_list.Insert_At_Beginning(11)
    L_list.Insert_At_Beginning(9)
    print("Linked List Before Rotation: ")
    L_list.Display()
    print("Linked List After Rotation: ")
    L_list.Rotation(4)
    L_list.Display()