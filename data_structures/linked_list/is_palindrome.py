"""
"A palindrome is a word, number, phrase, or other sequence of characters
which reads the same backward as forward, such as madam or racecar"
https://en.wikipedia.org/wiki/Palindrome
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def traverse(head):
    if head.next is None:
        return head.data
    else:
        return head.data+traverse(head.next)

def reverse(head):
    """
    Reverses the linked list IN PLACE and returns the new head
    >>> traverse(reverse(str2sll('abc')))=='cba'
    True
    >>> traverse(reverse(str2sll('0')))=='0'
    True
    """
    prev = None
    next_node=head

    # (1 -> 2 -> None) becomes (None <- 1 <- 2); return 2
    while current:= next_node:
        next_node = current.next
        current.next = prev
        prev = current
    # Return prev in order to put the head at the end
    return prev

def midpoint(head):
    """
    Finds the midpoint in N/2 iterations. That's still O(N)
    >>> l=str2sll('1234'); midpoint(l).data
    '3'
    >>> l=str2sll('12345'); midpoint(l).data
    '3'
    >>> l=str2sll('1'); midpoint(l).data
    '1'
    """
    slow = fast = head
    while fast and fast.next:
        fast, slow = fast.next.next, slow.next
    return slow

def is_palindrome(head):
    """
    >>> l=str2sll('abccba'); is_palindrome(l)
    True
    >>> l=str2sll('abcba'); is_palindrome(l)
    True
    >>> l=str2sll('abc'); is_palindrome(l)
    False
    """
    if not head:
        return True

    second=midpoint(head)

    second_rev = reverse(second)
    # compare two parts
    # len(second_rev)*2==len(head) or len(second_rev)*2 -1==len(head)
    while second_rev:
        if second_rev.data != head.data:
            return False
        second_rev = second_rev.next
        head = head.next
    return True

def is_palindrome_stack(head):
    """
    >>> l=str2sll('abccba'); is_palindrome_stack(l)
    True
    >>> l=str2sll('abcba'); is_palindrome_stack(l)
    True
    >>> l=str2sll('abc'); is_palindrome_stack(l)
    False
    """
    if not head or not head.next:
        return True

    second = midpoint(head)

    # Pushing the second half to a stack is equivalent to a reverse()
    stack = [second.data]
    while second.next:
        second = second.next
        stack.append(second.data)

    # Comparison
    while stack:
        if stack.pop() != head.data:
            return False
        head = head.next

    return True


def is_palindrome_dict(head):
    """
    >>> l=str2sll('aaabb'); is_palindrome_dict(l)
    False
    >>> l=str2sll('abccba'); is_palindrome_dict(l)
    True
    >>> l=str2sll('abcba'); is_palindrome_dict(l)
    True
    >>> l=str2sll('abc'); is_palindrome_dict(l)
    False
    """
    if not head or not head.next:
        return True
    d = {}
    pos = 0
    while head:
        d.setdefault(head.data, []).append(pos)
        head = head.next
        pos += 1
    checksum = pos - 1
    middle = 0
    for v in d.values():
        if len(v) % 2 != 0:
            middle += 1
        else:
            for step, pos in enumerate(v):
                if pos + v[len(v) - 1 - step] != checksum:
                    return False
        if middle > 1:
            return False
    return True


def str2sll(input: str) -> Node:
    """
    We assume that len(input)>=1
    >>> traverse(str2sll('abccba'))=='abccba'
    True
    >>> traverse(str2sll('0'))=='1'
    False
    """
    head = Node(input[0])
    cursor = head
    for char in input[1:]:
        cursor.next = Node(char)
        cursor = cursor.next
    return head


if __name__ == "__main__":
    from doctest import testmod

    testmod()
