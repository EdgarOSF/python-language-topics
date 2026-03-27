import logging

logging.basicConfig(level=logging.INFO)


class LoggedAgeAccess:
    def __get__(self, obj, objtype=None):
        value = obj._age
        logging.info('Accessin %r giving %r', 'age', value)
        return value

    def __set__(self, obj, value):
        logging.info('Update %r to %r', 'age', value)
        obj._age = value


class Person:
    age = LoggedAgeAccess()
    name = LoggedAgeAccess() 

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def birthday(self):
        self.age += 1
