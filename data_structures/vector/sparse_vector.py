__author__ = "Shota Nozadze"


class sparse_vector():

    # List initialization:
    # we pass number of zeros in the list
    # so, at first we have n zeros in the list
    # list[0] = 0; list[1] = 0 ... list[n-1] = 0
    # Sparse vector's strong side is
    # that we are saving memory
    # There is no 0s in the memory

    def __init__(self, n):
        self.data = list()
        self.zeros = n

    def push(self, i, val):
        incidx = False
        insertidx = -1
        nelem = (i, val)

        for idx in range(0, len(self.data)):
            elem = self.data[idx]
            if elem[0] >= i and incidx is False:
                self.data[idx] = (elem[0] + 1, elem[1])
                incidx = True
                insertidx = idx
            if incidx:
                self.data[idx] = (elem[0] + 1, elem[1])

        if incidx:
            self.data.insert(insertidx, nelem)
            return

        self.data.append(nelem)

    def get(self, i):
        for k in self.data:
            if k[0] == i:
                return k[1]
        return 0

    def count(self):
        return len(self.data) + self.zeros

    def print_vector(self):
        vec = ""
        for i in range(0, self.count()):
            vec += str(self.get(i)) + " | "
        print(vec)


if __name__ == "__main__":

    # 10 zeros
    # size: 10
    sv = sparse_vector(10)
    sv.print_vector()

    # on index 3 - 100
    # size: 11
    sv.push(3, 100)
    sv.print_vector()

    # index 3 - 100, index 5 - 69
    # size: 12
    sv.push(5, 69)
    sv.print_vector()

    # index 3 - 100, index 5 - 66, index 6 - 69
    # size: 13
    sv.push(5, 66)
    sv.print_vector()
