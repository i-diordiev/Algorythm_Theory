class ChainedHashDivision:
    table = []  # hash table
    size = 0  # size of hash table
    collision_counter = 0

    def __init__(self, n):  # constructor
        self.table = [[] for i in range(3 * n)]  # creating hash table which have 3x size of array
        self.size = 3 * n

    def HashFunction(self, element):  # hash function
        return element % self.size

    def Insert(self, element):
        pos = self.HashFunction(element)  # calculating index
        if len(self.table[pos]) > 0:  # if there is element in this cell, counter++
            self.collision_counter += 1
        self.table[pos].append(element)  # adding element to cell

    def Search(self, element):
        pos = self.HashFunction(element)  # calculating index
        for i in range(len(self.table[pos])):  # searching element in this cell
            if self.table[pos][i] == element:
                return pos
        return None

    def Delete(self, element):
        pos = self.HashFunction(element)  # calculating index
        self.table[pos].remove(element)
