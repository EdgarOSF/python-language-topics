class Archer:
    def __init__(self, hp, mana, arrows) -> None:
        self.hp = hp
        self.mana = mana
        self.arrows = arrows

    def shoot(self):
        if self.arrows < 0:
            print("No arrows left.")
        else:
            self.arrows -= 1
            print(f"Archer shot!. Arrows left: {self.arrows}")

    @classmethod
    def from_string(cls, data_str):
        hp, mana, arrows = list(map(int, data_str.split("-")))
        return cls(hp, mana, arrows)

    @staticmethod
    def static():
        print("Static method here!")

    def __str__(self) -> str:
        return f"Hp: {self.hp}, Mana: {self.mana}, Arrows: {self.arrows}"


archer1 = Archer(100, 100, 150)
print(archer1)

print()

archer2 = Archer.from_string("150-150-100")
print(archer2)

print()

Archer.static()
