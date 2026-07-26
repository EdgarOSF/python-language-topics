class AttackStrategy:
    def execute(self):
        pass


class AttackWithBows(AttackStrategy):
    def execute(self):
        print("Attacking with bow")


class AttackWithCrossbow(AttackStrategy):
    def execute(self):
        print("Attackin with Crossbow")


class Archer:
    def __init__(self, hp, strategy) -> None:
        self.hp = hp
        self.strategy = strategy

    def attack(self):
        return self.strategy.execute()


archer = Archer(100, AttackWithCrossbow())
print(archer)
archer.attack()
