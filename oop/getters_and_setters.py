class Archer:
    def __init__(self, hp, dmg) -> None:
        self._hp = hp
        self._dmg = dmg
        self.crit = 1.3
        self._overal_damage = None

    @property
    def dmg(self):
        return self._dmg

    @dmg.setter
    def dmg(self, value):
        self._overal_damage = None
        self._dmg = value

    @property
    def overal_damage(self):
        if self._overal_damage is None:
            self._overal_damage = self._dmg * self.crit
        return self._overal_damage

    @overal_damage.setter
    def overal_damage(self, value):
        raise ValueError("Overal damage cant be modified")


a1 = Archer(100, 20)
print(a1.dmg)
