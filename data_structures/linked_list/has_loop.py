@property
def has_loop(self) -> bool:
        """
        Detect whether the linked list contains a cycle using Floyd's
        Cycle-Finding Algorithm (Tortoise and Hare).

        Time Complexity: O(n)
        Auxiliary Space: O(1)
        """
        slow = self
        fast = self.next

        while fast is not None and fast.next is not None:
            if slow is fast:
                return True
            slow = slow.next
            fast = fast.next.next

        return False