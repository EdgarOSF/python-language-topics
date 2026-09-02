from time import perf_counter


class Temporizador:

    def __init__(self, etiqueta):
        self.etiqueta = etiqueta 
        self.segundos = None

    def __enter__(self):
        
        self.inicio = perf_counter()

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        fin = perf_counter()
        self.segundos = (fin - self.inicio)

        if exc_type is not None:
            print(f'Ocurrio un error con la etiqueta {self.etiqueta}')

        return False



with Temporizador("procesar datos") as timer:
    total = sum(range(1_000_000))

print(timer.etiqueta)  # procesar datos
print(timer.segundos)  # número mayor o igual a 0

with Temporizador("otra cosa") as timer:
    raise Exception

