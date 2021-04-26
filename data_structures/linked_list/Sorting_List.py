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

    def Sort(self):
        temp = self.head
        while(temp):
            minn = temp
            after = temp.next
            while(after):
                if minn.data > after.data:
                    minn = after
                after = after.next
            key = temp.data
            temp.data = minn.data
            minn.data = key
            temp = temp.next

    def Display(self):
        temp = self.head
        while(temp):
            print(temp.data, "->", end=" ")
            temp = temp.next
        print("None")


if __name__ == "__main__":
    L_list = Linked_List()
    L_list.Insert_At_End(8)
    L_list.Insert_At_End(5)
    L_list.Insert_At_End(10)
    L_list.Insert_At_End(7)
    L_list.Insert_At_End(6)
    L_list.Insert_At_End(11)
    L_list.Insert_At_End(9)
    print("Linked List: ")
    L_list.Display()
    print("Sorted Linked List: ")
    L_list.Sort()
    L_list.Display()
