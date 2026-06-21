class BinaryTrie:
    def __init__(self, max_bit_len=31):
        self.inf = 1 << 63
        self.cc = [0]
        self.to = [[-1], [-1]]
        self.mb = max_bit_len

    def add(self, a):
        u = 0
        self.cc[u] += 1
        for i in range(self.mb - 1, -1, -1):
            d = a >> i & 1
            if self.to[d][u] == -1:
                self.to[d][u] = len(self.cc)
                self.to[0].append(-1)
                self.to[1].append(-1)
                self.cc.append(0)
            u = self.to[d][u]
            self.cc[u] += 1

    def remove(self, a):
        if self.cc[0] == 0:
            return False
        uu = [0]
        u = 0
        for i in range(self.mb - 1, -1, -1):
            d = a >> i & 1
            u = self.to[d][u]
            if u == -1 or self.cc[u] == 0:
                return False
            uu.append(u)
        for u in uu:
            self.cc[u] -= 1
        return True

    def cnt(self, a):
        u = 0
        for i in range(self.mb - 1, -1, -1):
            d = a >> i & 1
            u = self.to[d][u]
            if u == -1 or self.cc[u] == 0:
                return 0
        return self.cc[u]

    def min_xor(self, a):
        if self.cc[0] == 0:
            return self.inf
        u, res = 0, 0
        for i in range(self.mb - 1, -1, -1):
            d = a >> i & 1
            v = self.to[d][u]
            if v == -1 or self.cc[v] == 0:
                res |= 1 << i
                u = self.to[d ^ 1][u]
            else:
                u = v
        return res

    def max_xor(self, a):
        if self.cc[0] == 0:
            return -self.inf
        u, res = 0, 0
        for i in range(self.mb - 1, -1, -1):
            d = a >> i & 1
            v = self.to[d ^ 1][u]
            if v == -1 or self.cc[v] == 0:
                u = self.to[d][u]
            else:
                u = v
                res |= 1 << i
        return res
