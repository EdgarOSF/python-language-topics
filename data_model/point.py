class Point:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f'Point({self.x}, {self.y})'

    def __str__(self) -> str:
        return f'{self.x}, {self.y}'


p = Point(2, 3)

print(p)
repr(p)