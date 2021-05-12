class OpenAddressHashLinear:
    table = []   # hash table
    size = 0  # size of hash table
    collision_counter = 0  # ...

    def __init__(self, n):  # constructor
        self.table = ["NIL" for i in range(3 * n)]  # creating hash table which have 3x size of array
        self.size = 3 * n

    def HashSupport(self, element):   # hash function
        return element % self.size

    def Insert(self, element):
        start_pos = self.HashSupport(element)  # start index of element
        for i in range(self.size):  # while element won't be written
            pos = (start_pos + i) % self.size  # calculate new index
            if i != 0:
                self.collision_counter += 1
            if self.table[pos] == "NIL" or self.table[pos] == "DEL":
                self.table[pos] = element
                break

    def Search(self, element):
        start_pos = self.HashSupport(element)  # start index of element
        for i in range(self.size):  # while element won't be found
            pos = (start_pos + i) % self.size  # calculate new index
            if element == self.table[pos]:
                return pos
            if self.table[pos] == "NIL":
                return None
        return None

    def Delete(self, element):
        start_pos = self.HashSupport(element)  # start index of element
        for i in range(self.size):  # while element won't be found
            pos = (start_pos + i) % self.size  # calculate new index
            if element == self.table[pos]:
                self.table[pos] = "DEL"
