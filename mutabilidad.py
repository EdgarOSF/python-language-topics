# class Usuario:
#     def __init__(self, nombre) -> None:
#         self.nombre = nombre
#
#
# usuario = Usuario("edgar")
# usuarios = {usuario}
# usuario.nombre = "omar"
# print(usuario in usuarios)
# usuario.nombre = "eduardo"
# print(usuario in usuarios)
# usuario.nombre = "carlos"
# print(usuario in usuarios)
# usuario.nombre = "davis"
# print(usuario in usuarios)
# usuario.nombre = "jose"
# print(usuario in usuarios)
# usuario.nombre = "daniela"
# print(usuario in usuarios)


# class Coordenada:
#     def __init__(self, x, y) -> None:
#         self.x = x
#         self.y = y


from dataclasses import dataclass


@dataclass(frozen=True)
class Coordenada:
    x: int
    y: int


origen = Coordenada(0, 0)

distancias = {origen: 0}
visitadas = {origen}

# print(Coordenada(0, 0) in visitadas)


class Carrito:
    def __init__(self) -> None:
        self.articulos = []

    def agregar(self, articulo):
        self.articulos.append(articulo)

    def __len__(self):
        return len(self.articulos)

    def __iter__(self):
        return iter(self.articulos)


carrito = Carrito()
carrito.agregar("manzana")
carrito.agregar("coca cola")

# for i in carrito:
#     print(i.upper())


it = iter(["A", "B"])

# print(next(it))
# print(next(it))
# print(next(it))


def pares_hasta(limite):

    for numero in range(0, limite + 1, 2):
        yield numero


pares = pares_hasta(6)

# print(next(pares))
# print(next(pares))
# print(next(pares))
# print(next(pares))


def mensajes():
    print("primero")
    yield "uno"
    print("segundo")
    yield "dos"


gen = mensajes()
# print("creado")
# print(next(gen))
# print(next(gen))


def cuadrados(numeros):
    for n in numeros:
        yield n * n


c = cuadrados([1, 2, 3])
print(list(c))
print(list(c))
