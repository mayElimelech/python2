class Octopus:
        count_animals = 0

        def __init__(self, name="Octavio"):
            self._name = name
            self._age = 0
            Octopus.count_animals += 1

        def birthday(self):
            self._age += 1

        def set_name(self, new_name):
            self._name = new_name

        def get_name(self):
            return self._name

        def get_age(self):
            return self._age
if __name__ == '__main__':
    oc1 = Octopus("may")
    oc2 = Octopus()

    oc1.set_name("elimelech")

    print(oc1.get_name()) 
    print(oc2.get_name())

    print(Octopus.count_animals)