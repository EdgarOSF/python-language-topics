class Archer:
    __slots__ = ("hp", "mana")

    def __init__(self, hp, mana) -> None:
        self.hp = hp
        self.mana = mana


class SuperArcher(Archer):
    def __init__(self, hp, mana, arrows) -> None:
        super().__init__(hp, mana)
        self.arrows = arrows


a1 = Archer(100, 50)
print(Archer.__dict__)
print(a1.hp, a1.mana)
print()
a2 = SuperArcher(100, 50, 20)
print(SuperArcher.__dict__)
print(a2.hp)
print(a2.mana)
print(a2.arrows)
