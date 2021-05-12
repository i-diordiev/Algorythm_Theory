class ChainedHashDivision:
    table = []
    size = 0
    collision_counter = 0

    def __init__(self, n):
        self.table = [[] for i in range(3 * n)]
        self.size = 3 * n

    def HashFunction(self, element):
        return element % self.size

    def Insert(self, element):
        pos = self.HashFunction(element)
        if len(self.table[pos]) > 0:
            self.collision_counter += 1
        self.table[pos].append(element)

    def Search(self, element):
        pos = self.HashFunction(element)
        for i in range(len(self.table[pos])):
            if self.table[pos][i] == element:
                return pos
        return None

    def Delete(self, element):
        pos = self.HashFunction(element)
        self.table[pos].remove(element)
