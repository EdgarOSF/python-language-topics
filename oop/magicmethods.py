import uuid


class Archer:
    def __init__(self, hp, mana, arrows) -> None:
        self.hp = hp
        self.mana = mana
        self.arrows = arrows
        self._id = uuid.uuid4()

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

    def __repr__(self) -> str:
        return f"Archer({self.hp}, {self.mana}, {self.arrows})"

    def __add__(self, other):
        if not isinstance(other, Archer):
            return NotImplemented
        new_hp = self.hp + other.hp
        new_mana = self.mana + other.mana
        new_arrows = self.arrows + other.arrows
        return Archer(new_hp, new_mana, new_arrows)

    def __eq__(self, other) -> bool:
        if not isinstance(other, Archer):
            return False
        return (
            self.hp == other.hp
            and self.mana == other.mana
            and self.arrows == other.arrows
        )

    def __gt__(self, other):
        if not isinstance(other, Archer):
            return NotImplemented
        return self.hp > other.hp

    def __hash__(self) -> int:
        return hash(self._id)


class Company:
    def __init__(self, size) -> None:
        self.size = size
        self.archers = []

    def __str__(self) -> str:
        return f"Company size: {len(self.archers)}, limit: {self.size}"

    # method add_archer:
    def add_archer(self, new_archer):
        # 0 - validamos que el objeto sea de un archer
        if not isinstance(new_archer, Archer):
            raise ValueError("Only Archers allowed")
        # 1 - verificamos que haya espacio en la compañia, sino retornamo ValueError
        if len(self.archers) == self.size:
            raise ValueError("Sorry, the company es full.")
        # 2 - agregamos al archer
        self.archers.append(new_archer)
        print("New archer is added")

    # magic method __add__()
    def __add__(self, archer):
        self.add_archer(archer)
        return self

    # magic method __iter__
    def __iter__(self):
        return iter(self.archers)

    def list_company(self):
        archers = [archer for archer in self.archers]
        print(archers)


archer1 = Archer(100, 100, 50)
print(archer1)
archer2 = Archer.from_string("80-100-10")
print(archer2)

print("Sum 2 archer:")
archer3 = archer1 + archer2
print(archer3)
print(f"{archer3=}")

print()

print(archer1 > archer2)
print(archer1 > archer3)

print()

print("Print hash")
print(hash(archer1))
print(hash(archer2))
print(hash(archer3))

print()

company1 = Company(2)
print(company1)
print("Add some archers...")
company1.add_archer(archer1)
company1.add_archer(archer2)

print()

company2 = Company(3)
newcompany = company2 + archer1 + archer3
print(newcompany)

print()

for archer in newcompany:
    print(archer)
