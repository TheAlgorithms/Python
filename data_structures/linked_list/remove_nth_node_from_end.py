class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def remove(head, n):
    extra = Node(0)
    extra.next = head
    fast = extra
    slow = extra
    for _ in range(n):
        fast = fast.next

    while fast.next:
        fast = fast.next
        slow = slow.next

    slow.next = slow.next.next

    return extra.next


def print_list(head):
    curr = head
    while curr:
        print(curr.val, end=" ")
        curr = curr.next


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(4)
head.next.next.next.next = Node(5)
print_list(head)
head = remove(head, 5)
print_list(head)
