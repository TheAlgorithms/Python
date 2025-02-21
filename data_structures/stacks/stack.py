'''
Benefits of This Version:
* Uses Exception instead of BaseException
* Uses deque for better performance
* Implements __len__() for Pythonic len(stack)
* Uses raise StackUnderflowError("Stack is empty") for better error messages
'''

from __future__ import annotations
from collections import deque
from typing import Generic, TypeVar

T = TypeVar("T")


class StackOverflowError(Exception):
    pass


class StackUnderflowError(Exception):
    pass


class Stack(Generic[T]):
    def __init__(self, limit: int = 10):
        self.stack: deque[T] = deque()
        self.limit = limit

    def __bool__(self) -> bool:
        return bool(self.stack)

    def __str__(self) -> str:
        return str(list(self.stack))

    def __len__(self) -> int:
        return len(self.stack)

    def push(self, data: T) -> None:
        if len(self.stack) >= self.limit:
            raise StackOverflowError("Stack is full")
        self.stack.append(data)

    def pop(self) -> T:
        if not self.stack:
            raise StackUnderflowError("Stack is empty")
        return self.stack.pop()

    def peek(self) -> T:
        if not self.stack:
            raise StackUnderflowError("Stack is empty")
        return self.stack[-1]

    def is_empty(self) -> bool:
        return not self.stack

    def is_full(self) -> bool:
        return len(self.stack) == self.limit

    def __contains__(self, item: T) -> bool:
        return item in self.stack
