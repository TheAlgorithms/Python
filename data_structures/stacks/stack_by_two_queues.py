from collections import deque
from typing import Generic, TypeVar

T = TypeVar("T")
""" Implementing stack using two arrays can be achieved in such a way that initially take two queue as insert queue and suffle queue then push the element in the insert queue followed by poping the elements from the suffle queue into the insert queue until the suffle queue becomes empty ,in that way if you visualise the algorithm the element you entered previously into the insert queue being the last element in case of Stack rule will be the first element of the insert queue and therefore popped first following the LIFO process """


class Stack(Generic[T]):  # Stack class to implement stack operations
    def __init__(self):
        self.insert_Queue = deque()  # First Queue to be used for inserting elements
        self.suffle_Queue = deque()  # Second Queue to be used for suffling

    def push(self, item: int):
        self.insert_Queue.append(item)  # Add items into the Queue
        while bool(self.suffle_Queue) == True:
            self.insert_Queue.append(
                self.suffle_Queue.popleft()
            )  # Poping the elements from the suffle queue into the insert queue in order

        self.insert_Queue, self.suffle_Queue = self.suffle_Queue, self.insert_Queue

    def pop(self):
        if (
            bool(self.suffle_Queue) == False
        ):  # if the stack or the suffle queue is empty
            return None
        return self.suffle_Queue.popleft()  # if not empty pop

    def top(self):
        if bool(self.suffle_Queue) == False:
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
            "Enter 1 to add elements in the stack 2 to pop and 3 to peek 4 to print the Stack and 5 to get the size of the stack and 6 to exit:"
        )
    )
    while n == 1 or n == 2 or n == 3 or n == 4 or n == 5 or n == 6:
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
                "Enter 1 to add elements in the stack 2 to pop and 3 to peek 4 to print the Stack and 5 to get the size of the stack and 6 to exit:"
            )
        )


if __name__ == "__main__":
    test_stack()  # calling the test funtion to test the process or the code
