def longest_consecutive_sequence(arr):
    heap = []
    for num in arr:
        heapq.heappush(heap, num)
    max_len = 0
    curr_len = 1
    while heap:
        num = heapq.heappop(heap)
        if heap and num == heap[0]-1:
            curr_len += 1
        elif curr_len > 1:
            max_len = max(max_len, curr_len)
            curr_len = 1
    if curr_len > 1:
        max_len = max(max_len, curr_len)
    return max_len
