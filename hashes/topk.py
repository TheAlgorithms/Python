"""
Given a non-empty list of words, return the k most frequent elements.
Your answer should be sorted by frequency from highest to lowest. 
If two words have the same frequency, then the word with the lower
alphabetical order comes first.
"""
import collections

def topk_frequent(self, words, k):
    """
    >> topk_frequent(["i", "love", "leetcode", "i", "love", "coding"], 2)
    ["i", "love"]
    """
    count = collections.Counter(words)
    freqMap = collections.defaultdict(list)
    
    for word, freq in count.items():
        freqMap[freq].append(word)
        
    freqs = list(freqMap.keys())
    heapq.heapify(freqs)
    
    topK = []
    for freq in heapq.nlargest(k, freqs):
        topK.extend(sorted(freqMap[freq]))
        if len(topK) >= k:
            return topK[:k]


if __name__ == "__main__":
    import doctest

    doctest.testmod()
