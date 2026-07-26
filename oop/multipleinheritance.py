# La multi herencia se determina por jerarquia, python busca
# la primera coincidencia del metodo walk y la encuentra en C
# ya que esta primero en el orden de herencia.
# class A:
#     def walk(self):
#         print("From A")
#
#     def met_1(self):
#         print("met_1 from A")
#
#     def walk_2(self):
#         print("metodo walk_2")
#
#
# class B(A):
#     def walk(self):
#         print("From B")
#
#
# class C(A):
#     def walk(self):
#         print("From C")
#
#     def met_1(self):
#         return super().met_1()
#
#
# class D(C, B, A):
#     pass
#
#
# obj = D()
# obj.walk()
# obj.met_1()
# obj.walk_2()

import json


class Archer:
    def __init__(self, hp) -> None:
        self.hp = hp

    def walk(self):
        return "I walk"


class ToJson:
    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)


class SuperWalkMixin:
    def walk(self):
        print(super().walk() + " very FAST!")


class SuperArcher(ToJson, Archer, SuperWalkMixin):
    pass


sa = SuperArcher(100)

print(sa.walk())
print(sa.to_json())
