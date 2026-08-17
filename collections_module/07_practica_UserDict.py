"""
Implementa una clase TypedUserDict que cumpla todas estas reglas:

* Las claves siempre se almacenan en minúsculas. ✅
* No se permiten claves vacías. ✅
* Los valores de tipo str se guardan con strip(). ✅
* Si el valor es una lista, cada elemento se limpia con strip() si es una cadena. ✅
* Mantén un historial (history) con cada operación de inserción, incluyendo la clave, el valor transformado y la fecha/hora. ✅
* Sobrescribe __missing__ para devolver "No encontrado" en lugar de lanzar KeyError.
* Haz que update() y setdefault() respeten todas las reglas anteriores.
"""

from collections import UserDict
from datetime import datetime
from typing import Any


class HistoryChanges:
    def __init__(self, key, value) -> None:
        self.key = key
        self.value = value
        self.date = datetime.now()

    def __str__(self) -> str:

        return f"""Change(key={self.key!r}, value={self.value!r}, date={self.date})"""


class TypedUserDict(UserDict):
    def __init__(self, *args, **kwargs) -> None:

        self.history: list[HistoryChanges] = list()

        super().__init__(*args, **kwargs)

    def __setitem__(self, key: str, item: Any) -> None:

        if not isinstance(key, str):
            raise TypeError("La clave debe ser una cadena")

        normalized_key = key.strip().lower()

        if not normalized_key:
            raise ValueError("No se permiten claves vacias.")

        if isinstance(item, str):
            item = item.strip()

        if isinstance(item, list):
            item = [
                value.strip() if isinstance(value, str) else value for value in item
            ]

        change = HistoryChanges(key=normalized_key, value=item)
        self.history.append(change)

        super().__setitem__(normalized_key, item)

    def __missing__(self, key):
        return "No encontrado"

    def __getitem__(self, key: Any):

        if isinstance(key, str):
            key = str(key).lower()

        return super().__getitem__(key)

    def __contains__(self, key: object) -> bool:

        if not isinstance(key, str):
            return False

        return super().__contains__(key.strip().lower())

    def get_history(self) -> list[HistoryChanges]:

        return self.history.copy()


mylist = TypedUserDict()

mylist["   A   "] = "  Edgar  "
mylist["lenguajes"] = ["Python", "Java", "Javascript"]

print(mylist)

print()

print("_____Historial_____")
for h in mylist.get_history():
    print(h)

print()

print("_____getitem____")
print(mylist["a"])
print(mylist["LENGUAJES"])
print(mylist["lEnGUajes"])

print()

print("_____Contains_____")
print("LENGUAJES" in mylist)
print("LeNgUAJeS" in mylist)

print()

print("____missing___")
print(mylist["no_existe"])

print()

print("____Clave vacia____")
mylist[""] = "omar"  # No se permiten claves vacias

