import os


class DirectorySize:
    def __get__(self, obj, objtype=None):
        return len(os.listdir(obj.dirname))


class Directory:
    size = DirectorySize()

    def __init__(self, dirname):
        self.dirname = dirname
