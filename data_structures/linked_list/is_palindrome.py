class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

    def get_data(self):
        return self.val

    def get_next(self):
        return self.next

    def set_next(self, new):
        self.next = new


class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def insert(self, val):
        new_node = Node(val)
        new_node.set_next(self.head)
        self.head = new_node


def is_palindrome(head):
    """
    Returns true if the linked list is a palindrome, false otherwise.
    Uses 2 pointers to traverse the linked list, reverses the second half
    and compares nodes on both sides of the split one by one
    >>> linked_list = LinkedList()
    >>> is_palindrome(linked_list.head)
    True
    >>> linked_list.insert(20)
    >>> linked_list.insert(11)
    >>> linked_list.insert(20)
    >>> is_palindrome(linked_list.head)
    True
    >>> linked_list = LinkedList()
    >>> linked_list.insert(20)
    >>> linked_list.insert(11)
    >>> linked_list.insert(11)
    >>> linked_list.insert(20)
    >>> is_palindrome(linked_list.head)
    True
    >>> linked_list.insert(20)
    >>> linked_list.insert(11)
    >>> linked_list.insert(20)
    >>> linked_list.insert(20)
    >>> is_palindrome(linked_list.head)
    False
    >>> linked_list = LinkedList()
    >>> linked_list.insert(12)
    >>> linked_list.insert(11)
    >>> linked_list.insert(20)
    >>> is_palindrome(linked_list.head)
    False
    """
    if not head:
        return True
    # split the list to two parts
    fast, slow = head.next, head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    second = slow.next
    slow.next = None  # Don't forget here! But forget still works!
    # reverse the second part
    node = None
    while second:
        nxt = second.next
        second.next = node
        node = second
        second = nxt
    # compare two parts
    # second part has the same or one less node
    while node:
        if node.val != head.val:
            return False
        node = node.next
        head = head.next
    return True


def is_palindrome_stack(head):
    """
    Returns true if the linked list is a palindrome, false otherwise
    Pushes nodes in the second half of the linked list
    one by one into a stack; once the stack is full,
    pop the node off the stack and compares
    it with nodes in the original list
    >>> linked_list = LinkedList()
    >>> is_palindrome_stack(linked_list.head)
    True
    >>> linked_list.insert(20)
    >>> linked_list.insert(11)
    >>> linked_list.insert(20)
    >>> is_palindrome_stack(linked_list.head)
    True
    >>> linked_list = LinkedList()
    >>> linked_list.insert(20)
    >>> linked_list.insert(11)
    >>> linked_list.insert(11)
    >>> linked_list.insert(20)
    >>> is_palindrome_stack(linked_list.head)
    True
    >>> linked_list.insert(20)
    >>> linked_list.insert(11)
    >>> linked_list.insert(20)
    >>> linked_list.insert(20)
    >>> is_palindrome_stack(linked_list.head)
    False
    >>> linked_list = LinkedList()
    >>> linked_list.insert(12)
    >>> linked_list.insert(11)
    >>> linked_list.insert(20)
    >>> is_palindrome_stack(linked_list.head)
    False
    """
    if not head or not head.next:
        return True

    # 1. Get the midpoint (slow)
    slow = fast = cur = head
    while fast and fast.next:
        fast, slow = fast.next.next, slow.next

    # 2. Push the second half into the stack
    stack = [slow.val]
    while slow.next:
        slow = slow.next
        stack.append(slow.val)

    # 3. Comparison
    while stack:
        if stack.pop() != cur.val:
            return False
        cur = cur.next

    return True


def is_palindrome_dict(head):
    """
    Returns true if the linked list is a palindrome, false otherwise
    Creates a dictionary of with the node's value
    as the key, and the list of positions
    of where this value occurs in the linked list as the value.
    Iterates through the list
    of values and checks that their indexes sum up to the length of the list - 1
    (ie same value at index 0 and l -1, same at 2 and l - 3 etc)
    >>> linked_list = LinkedList()
    >>> is_palindrome_dict(linked_list.head)
    True
    >>> linked_list.insert(20)
    >>> linked_list.insert(11)
    >>> linked_list.insert(20)
    >>> is_palindrome_dict(linked_list.head)
    True
    >>> linked_list = LinkedList()
    >>> linked_list.insert(20)
    >>> linked_list.insert(11)
    >>> linked_list.insert(11)
    >>> linked_list.insert(20)
    >>> is_palindrome_dict(linked_list.head)
    True
    >>> linked_list.insert(20)
    >>> linked_list.insert(11)
    >>> linked_list.insert(20)
    >>> linked_list.insert(20)
    >>> is_palindrome_dict(linked_list.head)
    False
    >>> linked_list = LinkedList()
    >>> linked_list.insert(12)
    >>> linked_list.insert(11)
    >>> linked_list.insert(20)
    >>> is_palindrome_dict(linked_list.head)
    False
    """
    if not head or not head.next:
        return True
    d = {}
    pos = 0
    while head:
        if head.val in d.keys():
            d[head.val].append(pos)
        else:
            d[head.val] = [pos]
        head = head.next
        pos += 1
    checksum = pos - 1
    middle = 0
    for v in d.values():
        if len(v) % 2 != 0:
            middle += 1
        else:
            step = 0
            for i in range(0, len(v)):
                if v[i] + v[len(v) - 1 - step] != checksum:
                    return False
                step += 1
        if middle > 1:
            return False
    return True
