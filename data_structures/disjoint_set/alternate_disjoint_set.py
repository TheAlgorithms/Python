"""
This code implements a disjoint set using Lists 
with added heuristics for efficiency
Union by Rank Heuristic and Path Compression
"""
class DisjointSet:
    def __init__(self, set_count):
        """
        Initialize with the number of items in each set
        and with rank = 1 for each set
        """
        self.set_count = set_count
        self.max_set = max(set_count)
        num_sets = len(set_count)
        self.ranks = [1] * num_sets
        self.parents = list(range(num_sets))

    def merge(self, src, dst):
        """
        union by rank
        """
        src_parent = self.get_parent(src)
        dst_parent = self.get_parent(dst)

        if src_parent == dst_parent:
            return False

        if self.ranks[dst_parent] >= self.ranks[src_parent]:
            self.set_count[dst_parent] += self.set_count[src_parent]
            self.set_count[src_parent] = 0
            self.parents[src_parent] = dst_parent
            if self.ranks[dst_parent] == self.ranks[src_parent]:
                self.ranks[dst_parent] += 1
            joined_set_size = self.set_count[dst_parent]
        else:
            self.set_count[src_parent] += self.set_count[dst_parent]
            self.set_count[dst_parent] = 0
            self.parents[dst_parent] = src_parent
            joined_set_size = self.set_count[src_parent]

        self.max_set = max(self.max_set, joined_set_size)
        return True

    def get_parent(self, set):
        """
        Find Parent and Compress Path
        """
        if self.parents[set] == set:
            return set
        self.parents[set] = self.get_parent(self.parents[set])
        return self.parents[set]
