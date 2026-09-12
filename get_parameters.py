class LoudNumber:
    def __init__(self, n):
        print(f'In LoadNumber.__init__, {n=}')
        self.n = n

    def __get__(self, obj, objtype):
        print(f'Also: {obj=}, {objtype=}')
        print(f'In LoadNumber.__get__, {self.n=}')
        return self.n


class Person:
    age = LoudNumber(30)


p = Person()
p.age
Person.age
