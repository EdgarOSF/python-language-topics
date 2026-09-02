from functools import update_wrapper

class ContadorLlamadas:
    def __init__(self, function):
        update_wrapper(self, function)
        self.llamadas = 0
        self.function = function

    def __call__(self, *args, **kwargs):
        self.llamadas += 1

        result = self.function(*args, **kwargs)

        return result


def cuadrado(numero):
    """Funcion que calcula el cuadrado de un numero"""

    return numero ** 2

cuadrado = ContadorLlamadas(cuadrado)

print(cuadrado(4))         # 16
print(cuadrado.llamadas)   # 1
print(cuadrado(5))         # 25
print(cuadrado.llamadas)   # 2
print(cuadrado.__name__)   # cuadrado



