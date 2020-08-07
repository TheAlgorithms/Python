# This algorithm has an incredible O(n) complexity!
# The elements that are not in order a simple eliminated!

def stalin_sort(seq):
    # seq = Any iterable sequence that supports .pop()
    for index in range(len(seq)):
        if index == len(seq)-1:
            return seq
        elif seq[index] > seq[index+1]:
            seq.pop(index)
        
            
