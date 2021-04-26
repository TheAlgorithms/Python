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

    def Add_two_no(self, First, Second):
        prev = None
        temp = None
        carry = 0
        while First is not None or Second is not None:
            first_data = 0 if First is None else First.data
            second_data = 0 if Second is None else Second.data
            Sum = carry+first_data+second_data
            carry = 1 if Sum >= 10 else 0
            Sum = Sum if Sum < 10 else Sum % 10
            temp = Node(Sum)
            if self.head is None:
                self.head = temp
            else:
                prev.next = temp
            prev = temp
            if First is not None:
                First = First.next
            if Second is not None:
                Second = Second.next
        if carry > 0:
            temp.next = Node(carry)

    def Display(self):
        temp = self.head
        while(temp):
            print(temp.data, "->", end=" ")
            temp = temp.next
        print("None")


if __name__ == "__main__":
    First = Linked_List()
    Second = Linked_List()
    First.Insert_At_Beginning(6)
    First.Insert_At_Beginning(4)
    First.Insert_At_Beginning(9)

    Second.Insert_At_Beginning(2)
    Second.Insert_At_Beginning(2)

    print("First Linked List: ")
    First.Display()
    print("Second Linked List: ")
    Second.Display()

    Result = Linked_List()
    Result.Add_two_no(First.head, Second.head)
    print("Final Result: ")
    Result.Display()
