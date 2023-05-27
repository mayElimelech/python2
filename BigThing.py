class BigThing:
    def __init__(self, data):
        self.data = data

    def size(self):
        if isinstance(self.data, (int, float)):
            return self.data
        else:
            return len(self.data)
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



if __name__ == '__main__':
    my_thing = BigThing("balloon")
    print(my_thing.size())
    cutie = BigCat("mitzy", 22)
    print(cutie.size())
