from abc import ABC, abstractmethod


class AbstractArcher(ABC):
    @abstractmethod
    def walk(self):
        print("Walking...")

    @property
    @abstractmethod
    def hp(self):
        pass


class Archer(AbstractArcher):
    def __init__(self, hp) -> None:
        self._hp = hp

    @property
    def hp(self):
        return self._hp

    def walk(self):
        super().walk()


a1 = Archer(100)
