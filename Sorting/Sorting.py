class Sorting:
    def __init__(self, input_array):
        self.sorting_array = input_array
        self.comparison_count = 0

    def merge(self, p, q, r):
        left = q - p + 1
        right = r - q
        left_arr = self.sorting_array[p:q + 1]
        right_arr = self.sorting_array[q + 1:r + 1]
        for i in range(left - 1):
            left_arr[i] = self.sorting_array[p + i]
        for j in range(right - 1):
            right_arr[j] = self.sorting_array[q + j + 1]
        i = 0
        j = 0
        k = p
        while i < left and j < right:
            if left_arr[i] <= right_arr[j]:
                self.comparison_count = self.comparison_count + 1
                self.sorting_array[k] = left_arr[i]
                i = i + 1
            else:
                self.comparison_count = self.comparison_count + 1
                self.sorting_array[k] = right_arr[j]
                j = j + 1
            k = k + 1
        while i < left:
            self.sorting_array[k] = left_arr[i]
            i = i + 1
            k = k + 1
        while j < right:
            self.sorting_array[k] = right_arr[j]
            j = j + 1
            k = k + 1

    def merge_sort(self, p, r):
        if p >= r:
            return -1
        q = (p + r) // 2
        self.merge_sort(p, q)
        self.merge_sort(q + 1, r)
        self.merge(p, q, r)
        return self.sorting_array, self.comparison_count

    
    def insertion_sort(self):
        for i in range(1, len(self.sorting_array)):
            key = self.sorting_array[i]
            j = i - 1
            if j >= 0 and self.sorting_array[j] < key:
                self.comparison_count = self.comparison_count + 1
            while j >= 0 and self.sorting_array[j] > key:
                self.comparison_count = self.comparison_count + 1
                self.sorting_array[j + 1] = self.sorting_array[j]
                j = j - 1
                if j >= 0 and self.sorting_array[j] < key:
                    self.comparison_count = self.comparison_count + 1
            self.sorting_array[j + 1] = key
        return self.sorting_array, self.comparison_count

    
    def heap(self, n, i):
        big = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and self.sorting_array[i] > self.sorting_array[left]:
            self.comparison_count = self.comparison_count + 1
        if left < n and self.sorting_array[i] < self.sorting_array[left]:
            self.comparison_count = self.comparison_count + 1
            big = left
        if right < n and self.sorting_array[big] > self.sorting_array[right]:
            self.comparison_count = self.comparison_count + 1
        if right < n and self.sorting_array[big] < self.sorting_array[right]:
            self.comparison_count = self.comparison_count + 1
            big = right
        if big != i:
            self.sorting_array[i], self.sorting_array[big] = self.sorting_array[big], self.sorting_array[i]
            self.heap(n, big)

    def heap_sort(self):
        n = len(self.sorting_array)
        for i in range(n // 2, -1, -1):
            self.heap(n, i)
        for i in range(n - 1, 0, -1):
            self.sorting_array[i], self.sorting_array[0] = self.sorting_array[0], self.sorting_array[i]
            self.heap(i, 0)
        return self.sorting_array, self.comparison_count
