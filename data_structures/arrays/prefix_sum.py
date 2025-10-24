class PrefixSum:
    def _init_(self, array: list[int]) -> None:
        len_array = len(array)
        self.prefix_sum = [0] * len_array
        if len_array > 0:
            self.prefix_sum[0] = array[0]
            for i in range(1, len_array):
                self.prefix_sum[i] = self.prefix_sum[i - 1] + array[i]

    def get_sum(self, start: int, end: int) -> int:
        # existing code...

    def contains_sum(self, target_sum: int) -> bool:
        # existing code...

if _name_ == "_main_":
    import doctest
    doctest.testmod()
