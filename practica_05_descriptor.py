class EnteroNoNegativo:

    def __set_name__(self, owner, name):
        self.public_name = name

    
    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        return obj.__dict__[self.public_name]


    def __set__(self, obj, value):
        
        if type(value) is not int:
            raise TypeError('El valor debe ser entero')
        elif value < 0:
            raise ValueError('El valor debe ser 0 o mayor')
            
        obj.__dict__[self.public_name] = value


class Inventario:
    cantidad = EnteroNoNegativo()
    limite = EnteroNoNegativo()

    def __init__(self, cantidad, limite):
        self.cantidad = cantidad
        self.limite = limite


inventario = Inventario(cantidad=10, limite=50)

print(inventario.cantidad)  # 10
print(inventario.limite)    # 50

inventario.cantidad = 15
print(inventario.cantidad)  # 15


try:
    inventario.cantidad = -1    # ValueError
except ValueError as e:
    print(e)

try:
    inventario.limite = "50"    # TypeError
except TypeError as e:
    print(e)
