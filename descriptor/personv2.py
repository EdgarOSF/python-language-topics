import logging

logging.basicConfig(level=logging.INFO)


class LoggedAccess:
    def __set_name__(self, owner, name):
        self.public_name = name
        self.private_name = '_' + name

    def __get__(self, ins, owner=None):
        value = getattr(ins, self.private_name)
        logging.info('Accessing %r giving %r', self.public_name, value)
        return value

    def __set__(self, ins, value):
        logging.info('Updated %r to %r', self.public_name, value)
        setattr(ins, self.private_name, value)


class Person:
    name = LoggedAccess()
    age = LoggedAccess()

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def birthdate(self):
        self.age += 1
