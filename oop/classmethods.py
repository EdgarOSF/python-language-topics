class Pizza:
    def __init__(self, ingredients) -> None:
        self.ingredients = ingredients

    @classmethod
    def hawaian(cls):
        return cls(["pineapple", "ham", "mozzarella", "tomatoes"])

    @classmethod
    def prosiutto(cls):
        return cls(["mozzarella", "tomatoes"])

    def __str__(self) -> str:
        return f"Piza with {' and '.join(self.ingredients)}"


print(Pizza.hawaian())

print()

print(Pizza.prosiutto())
