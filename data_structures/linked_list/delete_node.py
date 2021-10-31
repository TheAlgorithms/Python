from typing import Any
import doctest

class Node:
    def __init__(self, data: Any) -> None:
        self.data = data
        self.next = None
class Linkedlist:
    def __init__(self)-> None:
        self.head = None
    def push_at_head(self, data: Any) -> None:
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    # **deletion code starts**
    def delete_node(self, key) -> None:
        temp = self.head
        while temp.next:
            if temp.next.data == key:       #if next node is the node what we want to delete
                temp.next = temp.next.next  #breaking the link of node which has to be deleted
            temp = temp.next                #if condition not satisy then go to next node
    # **deletion code ends**
    def print_list(self) -> None:
        """
        >>> linked_list = Linkedlist()

        >>> linked_list.push_at_head(3)

        >>> linked_list.push_at_head(2)

        >>> linked_list.push_at_head(1)

        >>> linked_list.push_at_head(0)

        >>> linked_list.print_list()
        0->1->2->3->NULL

        >>> linked_list.delete_node(2)

        >>> linked_list.print_list()
        0->1->3->NULL
        
        """
        temp = self.head
        while temp:
            print(temp.data, end="->")
            temp = temp.next
        print("NULL")

if __name__=='__main__':
   
    doctest.testmod()
