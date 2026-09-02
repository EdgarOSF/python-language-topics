class RespuestaHTTP:

    __match_args__ = ('estado', 'cuerpo')

    def __init__(self, estado, cuerpo):
        
        if type(estado) is not int:
            raise TypeError('El codigo deber ser entero')
        if estado < 100 or estado > 599:
            raise ValueError('el codigo debe estar entre 100 y 599')

        if not isinstance(cuerpo, str):
            raise TypeError('El cuepor debe ser str')

        self._estado = estado
        self._cuerpo = cuerpo

    @property
    def estado(self):
        return self._estado

    @property
    def cuerpo(self):
        return self._cuerpo

    def __repr__(self):
        return f'RespuestaHTTP(estado={self._estado!r}, cuerpo={self._cuerpo!r})'

    

respuesta = RespuestaHTTP(404, "No encontrado")

match respuesta:
    case RespuestaHTTP(200, cuerpo):
        print(f"Éxito: {cuerpo}")
    case RespuestaHTTP(codigo, _) if 400 <= codigo < 500:
        print(f"Error del cliente: {codigo}")
    case RespuestaHTTP(estado=500, cuerpo=mensaje):
        print(f"Error del servidor: {mensaje}")

respuesta2 = RespuestaHTTP(200, "Cuerpo de exito")

match respuesta2:
    case RespuestaHTTP(200, cuerpo):
        print(f"Éxito: {cuerpo}")
    case RespuestaHTTP(codigo, _) if 400 <= codigo < 500:
        print(f"Error del cliente: {codigo}")
    case RespuestaHTTP(estado=500, cuerpo=mensaje):
        print(f"Error del servidor: {mensaje}")

respuesta3 = RespuestaHTTP(500, "Checate el backend")

match respuesta3:
    case RespuestaHTTP(200, cuerpo):
        print(f"Éxito: {cuerpo}")
    case RespuestaHTTP(codigo, _) if 400 <= codigo < 500:
        print(f"Error del cliente: {codigo}")
    case RespuestaHTTP(estado=500, cuerpo=mensaje):
        print(f"Error del servidor: {mensaje}")
try:
    RespuestaHTTP(99, "Inválida")      # ValueError
except ValueError as e:
    print(e)
try:
    RespuestaHTTP(600, "Inválida")     # ValueError
except ValueError as e:
    print(e)
try:
    respuesta.estado = 200             # AttributeError
except AttributeError as e:
    print(e)
