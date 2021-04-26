class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linked_List:
    def __init__(self):
        self.head = None

    def Insert_At_Beginning(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def Insert_After(self, node, new_data):
        if node is None:
            return "Alert!, Node must be in Linked List"
        new_node = Node(new_data)
        new_node.next = node.next
        node.next = new_node

    def Insert_At_End(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while(current.next):
            current = current.next
        current.next = new_node

    def Display(self):
        temp = self.head
        while(temp):
            print(temp.data, "->", end=" ")
            temp = temp.next
        print("None")


if __name__ == "__main__":
    L_list = Linked_List()
    L_list.Insert_At_Beginning(1)
    L_list.Display()
    L_list.Insert_At_Beginning(2)
    L_list.Display()
    L_list.Insert_At_Beginning(3)
    L_list.Display()
    L_list.Insert_At_End(4)
    L_list.Display()
    L_list.Insert_At_End(5)
    L_list.Display()
    L_list.Insert_At_End(6)
    L_list.Display()
    L_list.Insert_After(L_list.head.next, 10)
    L_list.Display()