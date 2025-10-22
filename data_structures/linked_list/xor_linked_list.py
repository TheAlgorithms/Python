"""
XOR Linked List implementation
A memory-efficient doubly linked list using XOR of node addresses.
Each node stores one pointer that is the XOR of previous and next node addresses.
Example:
>>> xor_list = XORLinkedList()
>>> xor_list.insert(10)
>>> xor_list.insert(20)
>>> xor_list.insert(30)
>>> xor_list.to_list()
[10, 20, 30]
"""

# Note: This implementation simulates pointer behavior using Python's id()
# and a dictionary lookup (_nodes). In languages like C, this would
# be done with actual memory addresses and pointer arithmetic.


class Node:
    def __init__(self, value: int):
        self.value = value
        self.both: int = 0  # XOR of prev and next node ids


class XORLinkedList:
    def __init__(self):
        # Use 'Node | None' instead of 'Optional[Node]' (per ruff UP045)
        self.head: Node | None = None
        self.tail: Node | None = None
        # id -> node map to simulate pointer references
        # In a low-level language, we would just store/use the memory addresses.
        self._nodes: dict[int, Node] = {}

    def _get_node(self, node_id: int) -> Node | None:
        """Helper to retrieve a node by its simulated ID."""
        return self._nodes.get(node_id)

    def _get_id(self, node: Node | None) -> int:
        """Helper to get the simulated ID (address) of a node."""
        return id(node) if node else 0

    def _xor(self, a: Node | None, b: Node | None) -> int:
        """Helper to XOR the IDs (addresses) of two nodes."""
        # Use 'Node | None' instead of 'Optional[Node]' (per ruff UP045)
        return self._get_id(a) ^ self._get_id(b)

    def insert(self, value: int) -> None:
        """Inserts a value at the end of the list."""
        node = Node(value)
        # Store the node in our simulated memory
        self._nodes[id(node)] = node

        if self.head is None:
            # List is empty
            self.head = node
            self.tail = node
            # node.both remains 0 (XOR of None and None)
        else:
            # List is not empty, append to tail
            # New node's 'both' points back to the old tail
            node.both = self._get_id(self.tail)
            
            # Update the old tail's 'both'
            # old_tail.both = (ID of node before old_tail) ^ (ID of new node)
            # We can get (ID of node before old_tail) by doing:
            # old_tail.both ^ (ID of next node, which was None/0)
            # So, old_tail.both ^ 0 = old_tail.both
            # new_tail.both = old_tail.both ^ self._get_id(node)
            
            # Simplified:
            # self.tail.both was (ID of prev_node) ^ 0
            # We need it to be (ID of prev_node) ^ (ID of new node)
            # So we XOR it with the new node's ID.
            if self.tail: # Type checker guard
                self.tail.both = self.tail.both ^ self._get_id(node)
            
            # Update the tail pointer
            self.tail = node

    def to_list(self) -> list[int]:
        """Converts the XOR linked list to a standard Python list (forward)."""
        result = []
        current = self.head
        prev_id = 0  # ID of the virtual 'None' node before head
        
        while current:
            result.append(current.value)
            
            # Get the ID of the next node
            # current.both = (ID of prev_node) ^ (ID of next_node)
            # So, (ID of next_node) = (ID of prev_node) ^ current.both
            next_id = prev_id ^ current.both
            
            # Move to the next node
            prev_id = self._get_id(current)
            current = self._get_node(next_id)
            
        return result


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    # Additional demonstration
    xor_list = XORLinkedList()
    xor_list.insert(10)
    xor_list.insert(20)
    xor_list.insert(30)
    print(f"List contents: {xor_list.to_list()}") # Output: [10, 20, 30]
    
    # Verify head and tail
    if xor_list.head:
        print(f"Head value: {xor_list.head.value}") # Output: 10
    if xor_list.tail:
        print(f"Tail value: {xor_list.tail.value}") # Output: 30