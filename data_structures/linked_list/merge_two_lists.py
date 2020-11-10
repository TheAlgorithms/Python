"""
Algorithm that merges two sorted linked lists into one sorted linked list.
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def create_linked_list(num_list: list) -> Node:
    """
    >>> node = create_linked_list([3,2,1])
    >>> node.data
    1
    >>> node = create_linked_list([9,6,-3,5,8])
    >>> node.data
    -3
    >>> create_linked_list([])

    """
    if not num_list:
        return None

    num_list.sort()
    current = head = Node(num_list[0])
    for i in range(1, len(num_list)):
        current.next = Node(num_list[i])
        current = current.next
    return head


def str_linked_list(head: Node) -> str:
    """
    >>> n1 = Node(1)
    >>> n2 = Node(2)
    >>> n3 = Node(3)
    >>> n1.next = n2
    >>> n2.next = n3
    >>> str_linked_list(n1)
    '1->2->3'
    """
    int_list = []
    current = head
    while current is not None:
        int_list.append(f"{current.data}")
        current = current.next
    return '->'.join(int_list)


def merge_lists(list_one: list, list_two: list) -> Node:
    """
    >>> n1 = Node(1)
    >>> n2 = Node(2)
    >>> n3 = Node(3)
    >>> n4 = Node(4)
    >>> n5 = Node(5)
    >>> n6 = Node(6)
    >>> n1.next = n3
    >>> n2.next = n4
    >>> n4.next = n5
    >>> n5.next = n6
    >>> ll = merge_lists(n1, n2)
    >>> str_linked_list(ll)
    '1->2->3->4->5->6'
    """
    node_one = list_one
    node_two = list_two
    merged_list = current_node = Node(0)

    while node_one is not None and node_two is not None:
        if node_one.data <= node_two.data:
            current_node.next = node_one
            node_one = node_one.next
        else:
            current_node.next = node_two
            node_two = node_two.next
        current_node = current_node.next

    if node_one is not None:
        current_node.next = node_one

    if node_two is not None:
        current_node.next = node_two

    return merged_list.next


def main() -> None:
    list1 = [3, 9, 7, 5, 1]
    list2 = [4, 6, 5, 2, 8, 7, 10, 3, 0]
    ll1 = create_linked_list(list1)
    ll2 = create_linked_list(list2)
    ll3 = merge_lists(ll1, ll2)
    print(str_linked_list(ll3))


if __name__ == "__main__":
    main()
    import doctest
    doctest.testmod()
