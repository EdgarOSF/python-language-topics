class Recurso:
    def __enter__(self):
        print("abriendo")
        return "recurso listo"

    def __exit__(self, tipo_error, error, traceback):
        print("Cerrando")


with Recurso() as recurso:
    print(recurso)


from contextlib import contextmanager


@contextmanager
def mensaje_temporal():
    print("antes")
    yield "disponible"
    print("despues")


with mensaje_temporal() as mensaje:
    print(mensaje)
