class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linked_List:
    def __init__(self):
        self.head = None

    def Insert_At_End(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while(current.next):
            current = current.next
        current.next = new_node

    def Delete(self, key):
        temp = self.head
        if temp is None:
            return "Can't Delete!"
        else:
            if temp.data == key:
                self.head = temp.next
                temp = None
        while temp is not None:
            prev = temp
            temp = temp.next
            curr = temp.next
            if temp.data == key:
                prev.next = curr
                return

    def Display(self):
        temp = self.head
        while(temp):
            print(temp.data, "->", end=" ")
            temp = temp.next
        print("None")


if __name__ == "__main__":
    L_list = Linked_List()
    L_list.Insert_At_End(1)
    L_list.Insert_At_End(2)
    L_list.Insert_At_End(3)
    L_list.Insert_At_End(4)
    L_list.Insert_At_End(5)
    L_list.Insert_At_End(6)
    L_list.Insert_At_End(7)
    print("Linked List: ")
    L_list.Display()
    print("Deleted Linked List: ")
    L_list.Delete(3)
    L_list.Display()
