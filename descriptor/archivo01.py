class Ten:
    def __get__(self, obj, objtype=None):
        print(self, obj, objtype)
        return 10


class A:
    x = 12
    y = Ten()
