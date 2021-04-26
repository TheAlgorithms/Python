class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Reverse_Linked_List:
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

    def Reverse_list_Groups(self, head, k):
        count = 0
        previous = None
        current = head
        while (current is not None and count < k):
            following = current.next
            current.next = previous
            previous = current
            current = following
            count += 1 
        if following is not None:
            head.next = self.Reverse_list_Groups(following, k)
        return previous

    def Display(self):
        temp = self.head
        while(temp):
            print(temp.data, "->", end=" ")
            temp = temp.next
        print("None")


if __name__ == "__main__":
    L_list = Reverse_Linked_List()
    L_list.Insert_At_End(1)
    L_list.Insert_At_End(2)
    L_list.Insert_At_End(3)
    L_list.Insert_At_End(4)
    L_list.Insert_At_End(5)
    L_list.Insert_At_End(6)
    L_list.Insert_At_End(7)
    L_list.Display()
    L_list.head = L_list.Reverse_list_Groups(L_list.head, 2)
    print("\nReverse Linked List: ")
    L_list.Display()