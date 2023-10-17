import heapq

def build_huffman_tree(char_freq):
    heap = [[weight, [char, ""]] for char, weight in char_freq.items()]
    heapq.heapify(heap)
    
    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
        
    return sorted(heapq.heappop(heap)[1:], key=lambda p: (len(p[-1]), p))

char_freq = {'a': 5, 'b': 9, 'c': 12, 'd': 13, 'e': 16, 'f': 45}
huffman_tree = build_huffman_tree(char_freq)

for char, code in huffman_tree:
    print(f"{char}: {code}")
