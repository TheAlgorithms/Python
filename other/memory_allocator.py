"""Memory allocator that provides an interface similar to the C standard library:
https://en.wikipedia.org/wiki/C_dynamic_memory_allocation . It uses a bytearray to
simulate the heap, which is controlled similarly to the sbrk() syscall.

It makes a heavy use of inheritance to progressively increase complexity without
duplicating code across implementations. That lowers barrier entry and allows the
comparison of test outputs, as all variations share the same interface.

Based on https://github.com/danluu/malloc-tutorial but added features like a more
advanced realloc() or alignment. Additionally, metadata is stored outside heap. This
design choice simplifies implementation in Python, since serialization and parsing
requires more steps compared to C, where such operations can be handled with simple
struct casting.
"""

import operator
from collections.abc import Iterable, Iterator
from dataclasses import dataclass, field
from typing import Self


class Heap:
    """The heap is a chunk of the virtual address space, typically used by libc for
    dynamic memory allocation. Its beginning is fixed, but its end can move, allowing it
    to grow or shrink. The point where heap ends is known as the 'program break'.

    https://en.wikipedia.org/wiki/Data_segment#Heap

    This is a simulation implemented as a constrained wrapper around a bytearray. It can
    only add or remove elements at the end.
    """

    def __init__(self):
        self.data = bytearray()

    def print(self, show_offset=False, bytes_per_row=4):
        """Pretty hexadecimal representation.

        >>> heap = Heap()
        >>> heap.data = bytearray(range(7))
        >>> heap.print()
        00 01 02 03
        04 05 06

        >>> heap.print(show_offset=True)
        0x00: 00 01 02 03
        0x04: 04 05 06
        """
        for offset in range(0, len(self.data), bytes_per_row):
            if show_offset:
                print(f"0x{offset:02X}: ", end="")
            values = " ".join(
                f"{c:02X}" for c in self.data[offset : offset + bytes_per_row]
            )
            print(values)

    def sbrk(self, increment: int) -> int:
        """Change the location of the program break and returns the previous location.
        Analogous to the C function with the same name.

        If the allocator calls this method with a positive/negative number, we
        will say that it has requested/returned memory to the operative system.

        >>> heap = Heap()
        >>> heap.data
        bytearray(b'')
        >>> heap.sbrk(2)
        0
        >>> heap.print()
        2E 2E
        >>> heap.sbrk(4)
        2
        >>> heap.print()
        2E 2E 2E 2E
        2E 2E

        To shrink pass a negative value:
        >>> heap.sbrk(-5)
        6
        >>> heap.print()
        2E
        """
        previous_program_break = len(self.data)

        if increment > 0:
            # Filling with something recognizable to facilitate debugging
            self.data.extend(b"." * increment)
        else:
            del self.data[:-increment]

        return previous_program_break

    def __len__(self):
        # This value should be minimized by a good memory allocator, as the OS uses
        # unallocated memory for other processes.
        return len(self.data)

    def __getitem__(self, index):
        # The IndexError exception raised here is analogous to the 'segmentation
        # fault' signal emitted by the OS
        return self.data[index]

    def __setitem__(self, index, value: int):
        if isinstance(index, slice):
            # The ability of slice assignment to add or remove elements in the middle,
            # altering the size of the bytearray, is not desired.
            raise ValueError("Can not use slice assignment")
        self.data[index] = value

    def strcpy(self, dst: int, src: Iterable[int]):
        """Copy from the given external bytes, to the specified location in the heap.
        The name is derived from the C function.

        >>> heap = Heap()
        >>> heap.data = bytearray(range(8))
        >>> heap.print()
        00 01 02 03
        04 05 06 07
        >>> heap.strcpy(3, [255] * 3)
        >>> heap.print()
        00 01 02 FF
        FF FF 06 07

        >>> heap.strcpy(4, range(5))
        Traceback (most recent call last):
          ...
        IndexError: bytearray index out of range
        """
        for index, value in enumerate(src):
            self.data[dst + index] = value


@dataclass
class MemoryAllocatorInterface:
    """These 3 methods are the most fundamental operations in
    https://en.wikipedia.org/wiki/C_dynamic_memory_allocation#Overview_of_functions

    All other methods added by subsequent implementations are either considered private
    or helpers for testing.
    """

    heap: Heap = field(default_factory=Heap)

    def malloc(self, size: int) -> int:
        """Allocate memory and returns the position in the heap where allocated memory
        starts.

        It is the client's responsibility not to access memory out of bounds.
        """
        raise NotImplementedError

    def free(self, pos: int):
        """Returns the block to the allocator so it can be reused. `pos` should
        be a value returned by malloc()

        It is client's responsibility not to access the region after this call.
        """
        raise NotImplementedError

    def realloc(self, pos: int, size: int) -> int:
        """Changes the size of an allocated region, either increasing or decreasing it

        Since there may not be enough space in the surrounding area to grow, it may move
        and return the position of the new location.
        """
        raise NotImplementedError


class MemoryAllocatorSimplest(MemoryAllocatorInterface):
    """
    >>> heap = Heap()
    >>> allocator = MemoryAllocatorSimplest(heap)

    >>> allocator.malloc(4)
    0
    >>> heap.strcpy(0, b'0000')
    >>> heap.print()
    30 30 30 30

    >>> allocator.malloc(2)
    4
    >>> heap.strcpy(4, b'11')
    >>> heap.print()
    30 30 30 30
    31 31

    So simple that it does not support free
    >>> allocator.free(4)
    Traceback (most recent call last):
      ...
    NotImplementedError
    """

    def malloc(self, size):
        return self.heap.sbrk(size)


@dataclass
class MemoryAllocatorFree(MemoryAllocatorInterface):
    """Support free() by storing the size of each allocated and freed block. This
    metadata will be stored in a linked list outside of the heap.

    >>> allocator = MemoryAllocatorFree()
    >>> _, p1, _ = [allocator.malloc_and_copy(d) for d in (b'00', b'1111', b'2222')]
    >>> allocator.heap.print()
    30 30 31 31
    31 31 32 32
    32 32
    >>> p1
    2
    >>> allocator.free(p1)
    >>> allocator.print()
    pos  size  free  data
      0     2        b'00'
      2     4     Y  b'1111'
      6     4        b'2222'
    >>> allocator.malloc_and_copy(b'333')
    2
    >>> allocator.print()
    pos  size  free  data
      0     2        b'00'
      2     4        b'3331'
      6     4        b'2222'

    The second block was reused, instead of growing the heap.
    """

    @dataclass
    class Block:
        size: int
        pos: int
        free: bool = False
        next: Self | None = None

        @property
        def is_last(self):
            return self.next is None

    first: Block | None = None

    def malloc(self, size):
        # Try to reuse an existing free block
        block = self.find_fit_block(size) or self.request_space(size)
        block.free = False
        return block.pos

    def free_block(self, block):
        assert not block.free
        block.free = True

    def free(self, pos):
        self.free_block(self.get(pos))

    def get(self, pos):
        # It would be quicker if a Dict[pos,Block] were maintained.
        return next(block for block in self.blocks if block.pos == pos)

    def find_fit_block(self, size) -> Block | None:
        try:
            return next(self.find_fit_blocks(size))
        except StopIteration:
            return None

    def find_fit_blocks(self, size) -> Iterator[Block]:
        return (block for block in self.blocks if block.free and block.size >= size)

    @property
    def blocks(self) -> Iterator[Block]:
        block = self.first
        while block:
            yield block
            block = block.next

    @property
    def is_empty(self):
        return self.first is None

    def get_last(self):
        *_, last = self.blocks
        return last

    def request_space(self, size) -> Block:
        """Grow the heap by requesting space to the OS."""
        new_block = self.Block(size=size, pos=self.heap.sbrk(size))
        self.linked_list_append(new_block)
        return new_block

    def linked_list_append(self, block):
        if self.is_empty:
            self.first = block
        else:
            last = self.get_last()
            last.next = block
        block.next = None

    def print(self):
        """To facilitate debugging"""
        fmt = "{pos:>3}  {size:>4}  {free:>4}  {data}"
        print(fmt.format(free="free", pos="pos", size="size", data="data"))
        for block in self.blocks:
            print(
                fmt.format(
                    free="Y" if block.free else "",
                    pos=block.pos,
                    size=block.size,
                    data=bytes(self.heap[block.pos : block.pos + block.size]),
                )
            )

    def malloc_and_copy(self, data: bytes) -> int:
        """Helper for tests"""
        pos = self.malloc(len(data))
        self.heap.strcpy(pos, data)
        return pos


class MemoryAllocatorSplit(MemoryAllocatorFree):
    """When reusing a block, split if it's larger than needed.

    >>> allocator = MemoryAllocatorSplit()
    >>> allocator.free(allocator.malloc(4))
    >>> allocator.print()
    pos  size  free  data
      0     4     Y  b'....'
    >>> allocator.malloc(2)
    0
    >>> allocator.print()
    pos  size  free  data
      0     2        b'..'
      2     2     Y  b'..'
    >>> allocator.malloc(2)
    2
    """

    def malloc(self, size):
        block = self.find_fit_block(size)
        if block:
            self.split(block, size)
        else:
            block = self.request_space(size)
        block.free = False
        return block.pos

    def split(self, block, size):
        if block.size <= size:
            return None
        new_block = self.Block(
            size=block.size - size, free=True, pos=block.pos + size, next=block.next
        )
        block.size = size  # shrink
        block.next = new_block  # insert in list
        return new_block


class MemoryAllocatorMerge(MemoryAllocatorSplit):
    """When freeing a block, attempt to merge it with the next one if it's free.

    >>> allocator = MemoryAllocatorMerge()
    >>> # allocator = MemoryAllocatorSplit() # uncomment to compare
    >>> p0 = allocator.malloc(2)
    >>> p1 = allocator.malloc(2)
    >>> allocator.free(p1)
    >>> allocator.free(p0)
    >>> allocator.print()
    pos  size  free  data
      0     4     Y  b'....'
    >>> allocator.malloc(4)
    0
    """

    def free_block(self, block):
        super().free_block(block)
        self.optimize_after_free(block)

    def optimize_after_free(self, block):
        self.merge_with_next(block)

    def merge_with_next(self, block):
        if block.next is None or not block.next.free:
            return
        block.size += block.next.size
        block.next = block.next.next

    def split(self, block, size):
        if new_block := super().split(block, size):
            self.optimize_after_free(new_block)
            return new_block


class MemoryAllocatorMergePrevious(MemoryAllocatorMerge):
    """Similar to the previous implementation, but also checks the previous block for
    merging.

    >>> allocator = MemoryAllocatorMergePrevious()
    >>> # allocator = MemoryAllocatorMerge() # uncomment to compare
    >>> p0 = allocator.malloc(2)
    >>> p1 = allocator.malloc(2)

    This time we revert the order to use the new feature:
    >>> allocator.free(p0)
    >>> allocator.free(p1)

    >>> allocator.malloc(4)
    0
    """

    # Now, the list must be doubly linked.
    @dataclass
    class Block(MemoryAllocatorMerge.Block):
        prev: Self | None = None

        @property
        def is_first(self):
            return self.prev is None

    def optimize_after_free(self, block):
        super().optimize_after_free(block)
        if block.prev and block.prev.free:
            self.merge_with_next(block.prev)

    def split(self, block, size):
        if new_block := super().split(block, size):
            new_block.prev = block
            return new_block

    def linked_list_append(self, block):
        old_last = self.get_last() if not self.is_empty else None
        super().linked_list_append(block)
        block.prev = old_last


class MemoryAllocatorAlign(MemoryAllocatorMergePrevious):
    """The address returned by malloc() is a multiple of 4.

    Data alignment improves performance at the CPU instruction level. That benefit is
    not demonstrated here. More info:
    https://en.wikipedia.org/wiki/Data_structure_alignment

    >>> allocator_this = MemoryAllocatorAlign()
    >>> allocator_prev = MemoryAllocatorMergePrevious()
    >>> for data in [b'333', b'4444', b'55555', b'1']:
    ...   _ = allocator_this.malloc_and_copy(data)
    ...   _ = allocator_prev.malloc_and_copy(data)

    >>> allocator_prev.heap.print(show_offset=True)
    0x00: 33 33 33 34
    0x04: 34 34 34 35
    0x08: 35 35 35 35
    0x0C: 31

    >>> allocator_this.heap.print(show_offset=True)
    0x00: 33 33 33 2E
    0x04: 34 34 34 34
    0x08: 35 35 35 35
    0x0C: 35 2E 2E 2E
    0x10: 31 2E 2E 2E

    The downside is that it takes more space.
    """

    @staticmethod
    def align(value: int, boundary=4) -> int:
        """
        >>> align = MemoryAllocatorAlign.align
        >>> align(3)
        4
        >>> align(4)
        4
        >>> align(5)
        8
        """
        res = (value // boundary) * boundary
        if res < value:
            res += boundary
        return res

    def malloc(self, size):
        return super().malloc(self.align(size))


class MemoryAllocatorRealloc(MemoryAllocatorMergePrevious):
    """
    >>> allocator = MemoryAllocatorRealloc()
    >>> [allocator.malloc_and_copy(d) for d in (b'AA', b'BBBB')]
    [0, 2]

    >>> allocator.print()
    pos  size  free  data
      0     2        b'AA'
      2     4        b'BBBB'
    >>> allocator.realloc(0, size=3)
    6
    >>> allocator.print()
    pos  size  free  data
      0     2     Y  b'AA'
      2     4        b'BBBB'
      6     3        b'AA.'
    """

    def realloc(self, pos, size):
        return self.realloc_block(self.get(pos), size)

    def realloc_block(self, block, size):
        # Simplest implementation: always copy
        new_pos = self.malloc(size)
        self.realloc_copy(dst=new_pos, src=block.pos, size=min(size, block.size))
        self.free_block(block)
        return new_pos

    def realloc_copy(self, dst: int, src: int, size):
        for i in range(size):
            self.heap[dst + i] = self.heap[src + i]


class MemoryAllocatorReallocShrink(MemoryAllocatorRealloc):
    """When a decrease is requested, avoid the potentially expensive call to
    realloc_copy()

    >>> allocator = MemoryAllocatorReallocShrink()
    >>> # allocator = MemoryAllocatorRealloc() # uncomment to compare
    >>> allocator.malloc(4)
    0
    >>> allocator.realloc(0, size=2)
    0
    >>> allocator.print()
    pos  size  free  data
      0     2        b'..'
      2     2     Y  b'..'
    """

    def realloc_block(self, block, new_size):
        if new_size <= block.size:
            self.split(block, new_size)
            return block.pos
        else:
            return super().realloc_block(block, new_size)


class MemoryAllocatorReallocExtend(MemoryAllocatorRealloc):
    """When more space is needed and the next block is free, try extending the current
    block instead of copying to a new location.

    >>> allocator = MemoryAllocatorReallocExtend()
    >>> allocator.malloc(2)
    0
    >>> allocator.free(allocator.malloc(2))
    >>> allocator.print()
    pos  size  free  data
      0     2        b'..'
      2     2     Y  b'..'
    >>> allocator.realloc(0, size=4)
    0
    >>> allocator.print()
    pos  size  free  data
      0     4        b'....'
    """

    def realloc_block(self, block, new_size):
        increase = new_size - block.size
        if (
            increase > 0
            and block.next
            and block.next.free
            and block.next.size >= increase
        ):
            self.merge_with_next(block)
            self.split(block, new_size)
            return block.pos
        return super().realloc_block(block, new_size)


class MemoryAllocatorReturnsMemoryToOS(MemoryAllocatorMergePrevious):
    """
    >>> allocator = MemoryAllocatorReturnsMemoryToOS()
    >>> [allocator.malloc(1) for i in range(3)]
    [0, 1, 2]
    >>> allocator.free(1)
    >>> allocator.print()
    pos  size  free  data
      0     1        b'.'
      1     1     Y  b'.'
      2     1        b'.'
    >>> allocator.free(2)
    >>> allocator.print()
    pos  size  free  data
      0     1        b'.'
    """

    def optimize_after_free(self, block):
        super().optimize_after_free(block)
        if block.is_last:
            self.shrink_heap()

    def shrink_heap(self):
        last = self.get_last() if not self.is_empty else None
        if last is not None and last.free:
            self.linked_list_remove_last()
            self.heap.sbrk(-last.size)

    def linked_list_remove_last(self):
        last = self.get_last()
        if last.is_first:
            # There was only this block,
            # the list is now empty.
            self.first = None
        else:
            new_last = last.prev
            new_last.next = None


class MemoryAllocatorBestFit(MemoryAllocatorFree):
    """When multiple blocks fit the requested size, choose the smallest one instead of
    the first one found.

    >>> allocator = MemoryAllocatorBestFit()
    >>> # allocator = MemoryAllocatorFree() # uncomment to compare
    >>> p0, _, p2, _ = map(allocator.malloc_and_copy, [b"A" * 8, b"B", b"CC", b"D"])
    >>> allocator.free(p0)
    >>> allocator.free(p2)
    >>> allocator.print()
    pos  size  free  data
      0     8     Y  b'AAAAAAAA'
      8     1        b'B'
      9     2     Y  b'CC'
     11     1        b'D'
    >>> allocator.malloc(2)
    9
    >>> allocator.malloc(8)
    0

    If you repeat the experiment with the previous implementation you will see that it
    has to grow the heap during the last malloc(), while this one doesn't. The reason is
    fragmentation: both have the same total free space, but divided in smaller holes,
    that can not be merged because they aren't contiguous.

    https://en.wikipedia.org/wiki/Fragmentation_(computing)#External_fragmentation
    """

    def find_fit_block(self, size):
        """Override first-fit implementation by best-fit."""
        blocks = list(self.find_fit_blocks(size))
        if not blocks:
            return None
        blocks.sort(key=operator.attrgetter("size"))
        return blocks[0]
