class D:
    def __set_name__(self, owner, name):
        self._name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self._name]

    def __set__(self, instance, value):
        if value < 0 or value > 100:
            raise ValueError("The value is not correct")
        instance.__dict__[self._name] = value


class Archer:
    hp = D
    mana = D

    def __init__(self, hp, mana) -> None:
        self.hp = hp
        self.mana = mana


a1 = Archer(100, 100)
print(a1.hp, a1.mana)
a1.mana = 50
print(a1.__dict__)

a2 = Archer(80, 80)
print(a2.__dict__)
a2.hp = 50
print(a2.__dict__)

print()

print(a1.__dict__)
print(a2.__dict__)
