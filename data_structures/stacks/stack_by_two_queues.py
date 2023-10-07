from collections import deque
from typing import Generic, TypeVar

T = TypeVar("T")
""" Implementing stack using two arrays  """


class Stack(Generic[T]):  # Stack class to implement stack operations
    def __init__(self):
        self.insert_Queue = deque()  # First Queue to be used for inserting
        self.suffle_Queue = deque()  # Second Queue to be used for suffling

    def push(self, item: int):
        self.insert_Queue.append(item)  # Add items into the Queue
        while self.suffle_Queue:
            self.insert_Queue.append(self.suffle_Queue.popleft())  # Poping the elements

        self.insert_Queue, self.suffle_Queue = self.suffle_Queue, self.insert_Queue

    def pop(self):
        if not (self.suffle_Queue):  # if the stack  is empty
            return None
        return self.suffle_Queue.popleft()  # if not empty pop

    def top(self):
        if not (self.suffle_Queue):
            return None
        return self.suffle_Queue[0]

    def printing(self):
        print(self.suffle_Queue)

    def size(self):
        return len(self.suffle_Queue)


def test_stack():
    s = Stack()  # Creating a stack in S
    n = int(
        input(
            "1 to push 2 to pop and 3 to peek 4 to print  and 5 for size of the stack and 6 to exit:"
        )
    )
    while n in (1, 2, 3, 4, 5, 6):
        match (n):
            case 1:
                element = int(input("Enter the element to push:"))
                s.push(element)
            case 2:
                print(s.pop())
            case 3:
                print(s.top())
            case 4:
                s.printing()
            case 5:
                leng = s.size()
                print(f"The size of the stack is {leng}")
            case 6:
                print("Exiting")
                break
            case _:
                print("Enter properly")

        n = int(
            input(
                "1 to push 2 to pop and 3 to peek 4 to print  and 5 for of the stack and 6 to exit:"
            )
        )


if __name__ == "__main__":
    test_stack()  # calling the test funtion
