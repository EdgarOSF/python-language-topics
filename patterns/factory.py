class Archer:
    def __init__(self, hp) -> None:
        self.hp = hp

    def walk(self):
        print("I'm walking")

    def attack(self):
        print("Shoot arrow!")


class Knight:
    def __init__(self, hp) -> None:
        self.hp = hp

    def walk(self):
        print("I'm marching")

    def attack(self):
        print("Swing the sword!")


def create_character(type: str, hp: int):
    if type == "Archer":
        return Archer(hp)
    if type == "Knight":
        return Knight(hp)


a1 = create_character("Archer", 100)
print(type(a1))
print(a1.__dict__)
a1.walk()
a1.attack()
print()

k1 = create_character("Knight", 200)
print(type(k1))
print(k1.__dict__)
k1.walk()
k1.attack()
