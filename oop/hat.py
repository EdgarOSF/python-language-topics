import random

class Hat:
    def __init__(self) -> None:
        self.house = ['Gryffindor', 'Hufflepuff', 'Ravenclaw', 'Slytherin']

    def sort(self, name):
        print(f'{name} is in {random.choice(self.house)}')


hat = Hat()
hat.sort("Harry")