class Dinero:
    def __init__(self, monto):
        self.monto = monto

    def __eq__(self, object):
        if isinstance(object, Dinero) and object.monto == self.monto:
            return True
        return False

    def __add__(self, object):
        if isinstance(object, Dinero):
            return Dinero(self.monto + object.monto)
        elif isinstance(object, (int, float)):
            return Dinero(object + self.monto)
        raise NotImplement('Tipo no soportado')

    def __radd__(self, other)
        return self.__add__(other)

    def __repr__(self):
        return f'Dinero({self.monto!r})'

precio = Dinero(100)
descuento = Dinero(25)

print(precio + descuento)  # Dinero(125)
print(precio + 10)         # Dinero(110)
#print(10 + precio)         # Dinero(110)
print(precio == Dinero(100))  # True
print(precio == 100)          # False

