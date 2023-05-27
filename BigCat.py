class BigCat(BigThing):
    def __init__(self, data, weight):
        super().__init__(data)
        self.weight = weight

    def size(self):
        if self.weight > 20:
            return "Very Fat"
        elif self.weight > 15:
            return "Fat"
        else:
            return "OK"

# Example usage
cutie = BigCat("mitzy", 22)
print(cutie.size())
