# class Bow:
#     def __init__(self, name, price, damage) -> None:
#         self.name = name
#         self.price = price
#         self.damage = damage
#
#
# bow1 = Bow("Edgar", 100, 100)
#
# print(bow1.__dict__)
#

# from dataclasses import dataclass
#
#
# @dataclass(frozen=True, order=True)
# class Bow:
#     name: str
#     price: float
#     damage: int
#
#
# bow1 = Bow("Edgar", 80.5, 100)
# bow2 = Bow("Edgar", 80.5, 100)
# bow3 = Bow("Omar", 80.5, 100)
# print(bow1)
# print(bow1 == bow2)  # __eq__ method
# print(bow1 == bow3)
# print(bow1 > bow3)  # order = True, __gt__ method
# bow1.price = "Carlos"  # frozen = True


from pydantic import BaseModel


class Bow(BaseModel):
    name: str
    price: float
    damage: int


# bow1 = Bow(name="Edgar", price=40.5, damage=10)
# print(bow1)

from enum import Enum


class Weapons(Enum):
    S = "Sword"
    B = "Bow"
    A = "Axe"
    SWORD = "Sword"


bow = Weapons("Bow")
# print(bow)
# print(bow.name)
# print(bow.value)
# print(Weapons.S)
# print(Weapons.B)
# print(Weapons.A)
# print(Weapons("Axe"))
# print(type(bow))
# print(isinstance(Weapons.S, Weapons))
# print(Weapons.S.value)
# print(bow.S is bow.SWORD)


class Armor(BaseModel):
    rooms: int
    weapons: list[Weapons]


armor1 = Armor(rooms=1, weapons=["Sword", "Bow"])
print(armor1.model_dump())
print(armor1)
