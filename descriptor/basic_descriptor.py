class Descriptor:
    def __set_name__(self, owner, name):
        self.private_name = '_' + name

    def __set__(self, instance, value):
        instance.__dict__[self.private_name] = value

    def __get__(self, instance, owner):
        if not instance:
            return self
        return instance.__dict__.get(self.private_name)

class Person:
    name = Descriptor()

