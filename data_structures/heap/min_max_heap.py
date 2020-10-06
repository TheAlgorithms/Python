class min_max_heap:
    """
    Implementation of the min-max heap, a detailed description can be found in:
    https://en.wikipedia.org/wiki/Min-max_heap

    All the methods work exactly as you would imagine.
    The get_* methods executes in O(1) time
    All other methods executes in O(log N) time.

    >>> h = min_max_heap()
    >>> for i in [3,0,6,3,4,7,0,0]:
    ...     h.insert(i)
    >>> print(h.get_min())
    0
    >>> print(h.get_max())
    7
    >>> result = []
    >>> for i in range(0, 4):
    ...     result.append(h.delete_min())
    >>> for i in range(0, 4):
    ...     result.append(h.delete_max())
    >>> print(result)
    [0, 0, 0, 3, 7, 6, 4, 3]
    """

    def __init__(self):
        self.__storage = []
        self.__size = 0

    def get_size(self):
        return self.__size

    def get_min(self):
        if self.__size == 0:
            return None
        else:
            return self.__storage[0]

    def get_max(self):
        if self.__size == 0:
            return None
        elif self.__size == 1:
            return self.__storage[0]
        elif self.__size == 2:
            return self.__storage[1]
        else:
            return max(self.__storage[1], self.__storage[2])

    def insert(self, value):
        if self.__size == len(self.__storage):
            self.__storage.append(0)
        self.__storage[self.__size] = value
        self.__size = self.__size + 1
        node_number = self.__size
        if self.__is_min_node(node_number):
            self.__bubble_up_min_node(node_number)
        else:
            self.__bubble_up_max_node(node_number)

    def delete_min(self):
        if self.__size == 0:
            return None
        result = self.__storage[0]
        self.__size = self.__size - 1
        self.__storage[0] = self.__storage[self.__size]
        self.__bubble_down_min_node(1)
        return result

    def delete_max(self):
        if self.__size == 0:
            return None
        elif self.__size == 1:
            result = self.__storage[0]
            self.__size = self.__size - 1
            return result
        elif self.__size == 2:
            result = self.__storage[1]
            self.__size = self.__size - 1
            return result
        else:
            if self.__storage[1] > self.__storage[2]:
                max_node_number = 2
            else:
                max_node_number = 3
            self.__size = self.__size - 1
            result = self.__storage[max_node_number - 1]
            self.__storage[max_node_number - 1] = self.__storage[self.__size]
            self.__bubble_down_max_node(max_node_number)
            return result

    def __has_parent_node(self, node_index):
        return node_index != 1

    def __parent_node(self, node_index):
        return node_index // 2

    def __is_min_node(self, node_index):
        if node_index == 1:
            return True
        else:
            return not self.__is_min_node(self.__parent_node(node_index))

    def __bubble_up_min_node(self, node_number):
        if self.__has_parent_node(node_number):
            max_node_number = self.__parent_node(node_number)
            if self.__storage[max_node_number - 1] < self.__storage[node_number - 1]:
                self.__swap(max_node_number - 1, node_number - 1)
                self.__bubble_up_max_node(max_node_number)
            elif self.__has_parent_node(max_node_number):
                min_node_number = self.__parent_node(max_node_number)
                if (
                    self.__storage[min_node_number - 1]
                    > self.__storage[node_number - 1]
                ):
                    self.__swap(min_node_number - 1, node_number - 1)
                    self.__bubble_up_min_node(min_node_number)

    def __bubble_up_max_node(self, node_number):
        if self.__has_parent_node(node_number):
            min_node_number = self.__parent_node(node_number)
            if self.__storage[min_node_number - 1] > self.__storage[node_number - 1]:
                self.__swap(min_node_number - 1, node_number - 1)
                self.__bubble_up_min_node(min_node_number)
            elif self.__has_parent_node(min_node_number):
                max_node_number = self.__parent_node(min_node_number)
                if (
                    self.__storage[max_node_number - 1]
                    < self.__storage[node_number - 1]
                ):
                    self.__swap(max_node_number - 1, node_number - 1)
                    self.__bubble_up_max_node(max_node_number)

    def __bubble_down_min_node(self, node_number):
        min_value = self.__storage[node_number - 1]
        is_next_node_type_max_node = True
        next_node_number = node_number
        for i in range(0, 2):
            candidate_node_number = node_number * 2 + i
            if candidate_node_number > self.__size:
                break
            else:
                candidate_value = self.__storage[candidate_node_number - 1]
                if candidate_value < min_value:
                    min_value = candidate_value
                    next_node_number = candidate_node_number
        for i in range(0, 4):
            candidate_node_number = node_number * 4 + i
            if candidate_node_number > self.__size:
                break
            else:
                candidate_value = self.__storage[candidate_node_number - 1]
                if candidate_value < min_value:
                    min_value = candidate_value
                    next_node_number = candidate_node_number
                    is_next_node_type_max_node = False
        if next_node_number != node_number:
            self.__swap(node_number - 1, next_node_number - 1)
            if is_next_node_type_max_node:
                self.__bubble_down_max_node(next_node_number)
            else:
                self.__bubble_down_min_node(next_node_number)

    def __bubble_down_max_node(self, node_number):
        max_value = self.__storage[node_number - 1]
        is_next_node_type_min_node = True
        next_node_number = node_number
        for i in range(0, 2):
            candidate_node_number = node_number * 2 + i
            if candidate_node_number > self.__size:
                break
            else:
                candidate_value = self.__storage[candidate_node_number - 1]
                if candidate_value > max_value:
                    max_value = candidate_value
                    next_node_number = candidate_node_number
        for i in range(0, 4):
            candidate_node_number = node_number * 4 + i
            if candidate_node_number > self.__size:
                break
            else:
                candidate_value = self.__storage[candidate_node_number - 1]
                if candidate_value > max_value:
                    max_value = candidate_value
                    next_node_number = candidate_node_number
                    is_next_node_type_min_node = False
        if next_node_number != node_number:
            self.__swap(node_number - 1, next_node_number - 1)
            if is_next_node_type_min_node:
                self.__bubble_down_min_node(next_node_number)
            else:
                self.__bubble_down_max_node(next_node_number)

    def __swap(self, left, right):
        temp = self.__storage[left]
        self.__storage[left] = self.__storage[right]
        self.__storage[right] = temp


if __name__ == "__main__":
    import doctest

    doctest.testmod()
