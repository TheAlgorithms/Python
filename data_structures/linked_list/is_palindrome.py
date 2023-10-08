def is_palindrome(head):
    """
    Check if a linked list is a palindrome.

    Args:
        head (ListNode): The head of the linked list.

    Returns:
        bool: True if the linked list is a palindrome, False otherwise.

    Examples:
        >>> is_palindrome(None)
        True

        >>> is_palindrome(ListNode(1))
        True

        >>> is_palindrome(ListNode(1, ListNode(2)))
        False

        >>> is_palindrome(ListNode(1, ListNode(2, ListNode(1))))
        True

        >>> is_palindrome(ListNode(1, ListNode(2, ListNode(2, ListNode(1)))))
        True
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
    Check if a linked list is a palindrome using a stack.

    Args:
        head (ListNode): The head of the linked list.

    Returns:
        bool: True if the linked list is a palindrome, False otherwise.

    Examples:
        >>> is_palindrome_stack(None)
        True

        >>> is_palindrome_stack(ListNode(1))
        True

        >>> is_palindrome_stack(ListNode(1, ListNode(2)))
        False

        >>> is_palindrome_stack(ListNode(1, ListNode(2, ListNode(1))))
        True

        >>> is_palindrome_stack(ListNode(1, ListNode(2, ListNode(2, ListNode(1)))))
        True
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
    Check if a linked list is a palindrome using a dictionary.

    Args:
        head (ListNode): The head of the linked list.

    Returns:
        bool: True if the linked list is a palindrome, False otherwise.

    Examples:
        >>> is_palindrome_dict(None)
        True

        >>> is_palindrome_dict(ListNode(1))
        True

        >>> is_palindrome_dict(ListNode(1, ListNode(2)))
        False

        >>> is_palindrome_dict(ListNode(1, ListNode(2, ListNode(1))))
        True

        >>> is_palindrome_dict(ListNode(1, ListNode(2, ListNode(2, ListNode(1)))))
        True
    """
    if not head or not head.next:
        return True
    d = {}
    pos = 0
    while head:
        if head.val in d:
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
            for i in range(len(v)):
                if v[i] + v[len(v) - 1 - step] != checksum:
                    return False
                step += 1
        if middle > 1:
            return False
    return True

if __name__ == "__main__":
    import doctest

    doctest.testmod()