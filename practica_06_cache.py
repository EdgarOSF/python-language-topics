from functools import cached_property


class AnalizadorTexto:

    def __init__(self, cadena):
        self.texto = cadena
        self._calculos = 0

    @property
    def texto(self):
        return self._texto

    @texto.setter
    def texto(self, valor):
        if not isinstance(valor, str):
            raise TypeError('El valor tiene que ser str')
        self._texto = valor

        try:
            del self.conteo_palabras
        except AttributeError:
            pass

    @cached_property
    def conteo_palabras(self):
        self._calculos += 1
        return len(self.texto.split())

    @property
    def calculos(self):
        return self._calculos


analizador = AnalizadorTexto("Python es simple")
try:
    analizador.texto = 12
except TypeError as e:
    print(e)


print(analizador.conteo_palabras)  # 3
print(analizador.conteo_palabras)  # 3; debe reutilizar la caché
print(analizador.conteo_palabras)  # 3; debe reutilizar la caché
print(analizador.calculos)         # 1

analizador.texto = "Python también es potente"

print(analizador.conteo_palabras)  # 4; debe recalcularse
print(analizador.calculos)         # 2
