class ConfiguracionApp:

    instance = None

    def __new__(cls, entorno):

        if not isinstance(entorno, str):
            raise TypeError('"entorno" debe ser una cadena')
        
        if entorno == '':
            raise ValueError('"entorno" no debe ser vacio')
        
        if cls.instance is None:
            cls.instance = super().__new__(cls)

        return cls.instance

    def __init__(self, entorno):
        if 'entorno' not in self.__dict__:
            self.entorno = entorno

    def __repr__(self):
        return f'ConfiguracionApp(entorno={self.entorno!r})'
    

primera = ConfiguracionApp('produccion')
segunda = ConfiguracionApp('desarrollo')

print(primera is segunda)       # True
print(primera.entorno)          # produccion
print(segunda.entorno)          # produccion


try:
    tercera = ConfiguracionApp(True)
    cuarta = ConfiguracionApp(1)
except Exception as e:
    print(e)

