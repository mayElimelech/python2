class Animal:
    zoo_name = "Hayaton"

    def __init__(self, name, hunger=0):
        self.name = name
        self.hunger = hunger

    def get_name(self):
        return self.name

    def is_hungry(self):
        return self.hunger > 0

    def feed(self):
        if self.is_hungry():
            self.hunger -= 1

    def talk(self):
        pass


class Dog(Animal):
    def talk(self):
        print("woof woof")

    def fetch_stick(self):
        print("There you go, sir!")

class Cat(Animal):
    def talk(self):
        print("Meow")
    def chase_laser(self):
        print("Meeeeow")


class Skunk(Animal):
    def __init__(self, name, hunger=0):
        super().__init__(name, hunger)
        self._stink_count = 6

    def talk(self):
        print("tsssss")

    def stink(self):
        print("Dear Lord!")


class Unicorn(Animal):
    def __init__(self, name, hunger=0):
        super().__init__(name, hunger)
        self._color = "Green"

    def talk(self):
        print("Good day, darling")

    def sing(self):
        print("I'm not your toy...")


class Dragon(Animal):
    def __init__(self, name, hunger=0):
        super().__init__(name, hunger)
        self._color = "Green"

    def talk(self):
        print("Raaaawr")

    def breath_fire(self):
        print("$@#$#@$")


def main():
    zoo_lst = [
        Dog("Brownie", 10),
        Cat("Zelda", 3),
        Skunk("Stinky"),
        Unicorn("Keith", 7),
        Dragon("Lizzy", 1450),

    ]
    zoo_lst.append( Dog("Doggo", 80))
    zoo_lst.append( Cat("Kitty", 80))
    zoo_lst.append(Skunk("Stinky Jr.", 80))
    zoo_lst.append(Unicorn("Clair", 80))
    zoo_lst.append(Dragon("McFly", 80))

    for animal in zoo_lst:
        print(animal.__class__.__name__,animal.get_name())
        while animal.is_hungry():
            animal.feed()
        animal.talk()
        if isinstance(animal, Dog):
            animal.fetch_stick()
        elif isinstance(animal, Cat):
            animal.chase_laser()
        elif isinstance(animal, Skunk):
            animal.stink()
        elif isinstance(animal, Unicorn):
            animal.sing()
        elif isinstance(animal, Dragon):
            animal.breath_fire()

    print(Animal.zoo_name)


if __name__ == "__main__":
    main()
