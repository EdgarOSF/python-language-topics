from Vector2d import Vector


# Los componentes de Vector pueden ser accedidos como atributos
v1 = Vector(3,4)
print(v1.x, v1.y)

# Desempaquetar, pero para que funcione como iterable tiene que implementar el metodo __iter__
x, y = v1
print(x, y)


# Acceder por indice, pero para que funcione tiene que implementar el metodo "__getitem__"
print(v1[0], v1[1])