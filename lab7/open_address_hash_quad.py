class OpenAddressHashQuad:
    table = []
    size = 0
    c1 = 0.5
    c2 = 1
    collision_counter = 0

    def __init__(self, n):
        self.table = ["NIL" for i in range(3 * n)]
        self.size = 3 * n

    def HashSupport(self, element):
        return element % self.size

    def Insert(self, element):
        start_pos = self.HashSupport(element)
        for i in range(self.size):
            pos = int((start_pos + (self.c1 * i) + (self.c2 * i * i))) % self.size
            if i != 0:
                self.collision_counter += 1
            if self.table[pos] == "NIL" or self.table[pos] == "DEL":
                self.table[pos] = element
                break

    def Search(self, element):
        start_pos = self.HashSupport(element)
        for i in range(self.size):
            pos = int((start_pos + (self.c1 * i) + (self.c2 * i * i))) % self.size
            if element == self.table[pos]:
                return pos
            if self.table[pos] == "NIL":
                return None
        return None

    def Delete(self, element):
        start_pos = self.HashSupport(element)
        for i in range(self.size):
            pos = int((start_pos + (self.c1 * i) + (self.c2 * i * i))) % self.size
            if element == self.table[pos]:
                self.table[pos] = "DEL"
