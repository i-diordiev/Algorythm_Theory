class OpenAddressHashDouble:
    table = []
    size = 0
    collision_counter = 0

    def __init__(self, n):
        self.table = ["NIL" for i in range(3 * n)]
        self.size = 3 * n

    def Hash1(self, element):
        return element % self.size

    def Hash2(self, element):
        return 1 + (element % self.size)

    def Insert(self, element):
        start_pos = self.Hash1(element)
        second_pos = self.Hash2(element)
        for i in range(self.size):
            pos = (start_pos + i * second_pos) % self.size
            if i != 0:
                self.collision_counter += 1
            if self.table[pos] == "NIL" or self.table[pos] == "DEL":
                self.table[pos] = element
                break

    def Search(self, element):
        start_pos = self.Hash1(element)
        second_pos = self.Hash2(element)
        for i in range(self.size):
            pos = (start_pos + i * second_pos) % self.size
            if element == self.table[pos]:
                return pos
            if self.table[pos] != "NIL":
                return None
        return None

    def Delete(self, element):
        start_pos = self.Hash1(element)
        second_pos = self.Hash2(element)
        for i in range(self.size):
            pos = (start_pos + i * second_pos) % self.size
            if element == self.table[pos]:
                self.table[pos] = "DEL"
