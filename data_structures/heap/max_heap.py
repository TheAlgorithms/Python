class Heap(object):
    def __init__(self):
        self.__array = []
        self.__last_index = -1

    def push(self, value):
        """
            Append item on the back of the heap,
            sift upwards if heap property is violated.
        """
        self.__array.append(value)
        self.__last_index += 1
        self.__siftup(self.__last_index)

    def pop(self):
        """
            Pop root element from the heap (if possible),
            put last element as new root and sift downwards till
            heap property is satisfied.

        """
        if self.__last_index == -1:
            raise IndexError("Can't pop from empty heap")
        root_value = self.__array[0]
        if self.__last_index > 0:  # more than one element in the heap
            self.__array[0] = self.__array[self.__last_index]
            self.__siftdown(0)
        self.__last_index -= 1
        return root_value

    def peek(self):
        """ peek at the root, without removing it """
        if not self.__array:
            return None
        return self.__array[0]

    def replace(self, new_value):
        """ remove root & put NEW element as root & sift down -> no need to sift up """
        if self.__last_index == -1:
            raise IndexError("Can't pop from empty heap")
        root_value = self.__array[0]
        self.__array[0] = new_value
        self.__siftdown(0)
        return root_value

    def heapify(self, input_list):
        """
            each leaf is a trivial subheap, so we may begin to call
            Heapify on each parent of a leaf.  Parents of leaves begin
            at index n/2.  As we go up the tree making subheaps out
            of unordered array elements, we build larger and larger
            heaps, joining them at the i'th element with Heapify,
            until the input list is one big heap.
        """
        n = len(input_list)
        self.__array = input_list
        self.__last_index = n-1
        for index in reversed(range(n//2)):
            self.__siftdown(index)

    @classmethod
    def createHeap(cls, input_list):
        """
            create an heap based on an inputted list.
        """
        heap = cls()
        heap.heapify(input_list)
        return heap

    def __siftdown(self, index):
        current_value = self.__array[index]
        left_child_index, left_child_value = self.__get_left_child(index)
        right_child_index, right_child_value = self.__get_right_child(index)
        # the following works because if the right_child_index is not None, then the left_child
        # is also not None => property of a complete binary tree, else left will be returned.
        best_child_index, best_child_value = (right_child_index, right_child_value) if right_child_index\
        is not None and self.comparer(right_child_value, left_child_value) else (left_child_index, left_child_value)
        if best_child_index is not None and self.comparer(best_child_value, current_value):
            self.__array[index], self.__array[best_child_index] =\
                best_child_value, current_value
            self.__siftdown(best_child_index)
        return


    def __siftup(self, index):
        current_value = self.__array[index]
        parent_index, parent_value = self.__get_parent(index)
        if index > 0 and self.comparer(current_value, parent_value):
            self.__array[parent_index], self.__array[index] =\
                current_value, parent_value
            self.__siftup(parent_index)
        return

    def comparer(self, value1, value2):
        raise NotImplementedError("Should not use the baseclass heap\
            instead use the class MinHeap or MaxHeap.")

    def __get_parent(self, index):
        if index == 0:
            return None, None
        parent_index =  (index - 1) // 2
        return parent_index, self.__array[parent_index]

    def __get_left_child(self, index):
        left_child_index = 2 * index + 1
        if left_child_index > self.__last_index:
            return None, None
        return left_child_index, self.__array[left_child_index]

    def __get_right_child(self, index):
        right_child_index = 2 * index + 2
        if right_child_index > self.__last_index:
            return None, None
        return right_child_index, self.__array[right_child_index]

    def __repr__(self):
        return str(self.__array[:self.__last_index+1])

    def __eq__(self, other):
        if isinstance(other, Heap):
            return self.__array == other.__array
        if isinstance(other, list):
            return self.__array == other
        return NotImplemented


class MaxHeap(Heap):
    def comparer(self, value1, value2):
        return value1 > value2