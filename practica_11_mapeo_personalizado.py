from collections.abc import MutableMapping


class Inventario(MutableMapping):

    def __init__(self, items):
        self._items = dict()
        for key, value in items.items():
            self.__setitem__(key, value)

    def __getitem__(self, index):
        return self._items[index]

    def __setitem__(self, key, value):
        self._validar(key, value)
        self._items[key] = value

    def __delitem__(self, key):
        del self._items[key]

    def __len__(self):
        return len(self._items)

    def __iter__(self):
        return iter(self._items)

    @property
    def total_unidades(self):
        return sum(self._items.values())

    def _validar(self, key, value):
        if not isinstance(key, str):
            raise TypeError('La clave debe ser str')
        if key == '':
            raise ValueError('La key no puede estar vacia')
        if type(value) is not int:
            raise TypeError('Los valores deben ser enteros')
        if value < 0:
            raise ValueError('Los valores no pueden ser menores de cero')



inventario = Inventario({"manzana": 3, "pera": 2})

print(inventario["manzana"])  # 3

inventario["pera"] = 5
inventario["naranja"] = 1

print(len(inventario))              # 3
print(list(inventario))             # ["manzana", "pera", "naranja"]
print(inventario.total_unidades)    # 9

del inventario["manzana"]
print("manzana" in inventario)      # False
