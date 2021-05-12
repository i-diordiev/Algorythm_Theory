class OpenAddressHashDouble:
    table = []  # hash table
    size = 0  # size of hash table
    collision_counter = 0  # ...

    def __init__(self, n):  # counstructor
        self.table = ["NIL" for i in range(3 * n)]  # creating hash table which have 3x size of array
        self.size = 3 * n

    def Hash1(self, element):  # first hash function
        return element % self.size

    def Hash2(self, element):  # second hash function
        return 1 + (element % self.size)

    def Insert(self, element):
        start_pos = self.Hash1(element)  # start index of element
        second_pos = self.Hash2(element)
        for i in range(self.size):  # while element won't be written
            pos = (start_pos + i * second_pos) % self.size  # calculate new index using 2 hash functions
            if i != 0:
                self.collision_counter += 1
            if self.table[pos] == "NIL" or self.table[pos] == "DEL":
                self.table[pos] = element
                break

    def Search(self, element):
        start_pos = self.Hash1(element)  # start index of element
        second_pos = self.Hash2(element)
        for i in range(self.size):  # while element won't be found
            pos = (start_pos + i * second_pos) % self.size  # calculate new index using 2 hash functions
            if element == self.table[pos]:
                return pos
            if self.table[pos] != "NIL":
                return None
        return None

    def Delete(self, element):
        start_pos = self.Hash1(element)  # start index of element
        second_pos = self.Hash2(element)
        for i in range(self.size):  # while element won't be found
            pos = (start_pos + i * second_pos) % self.size  # calculate new index using 2 hash functions
            if element == self.table[pos]:
                self.table[pos] = "DEL"
