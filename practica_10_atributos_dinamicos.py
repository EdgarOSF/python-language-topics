class Configuracion:
    def __init__(self, attrs):

       for key in attrs:
           if not isinstance(key, str):
               raise TypeError('La clave debe ser str')

       super().__setattr__('_values', dict(attrs))

    def __getattr__(self, key):
        if key in self._values:
            return self._values[key]
        raise AttributeError(f'No existe la configuración: {key}')

    def __setattr__(self, name, value):

        if name in self._values.keys():
            raise ValueError(f'La configuracion {name} no puede ser reasignada')
        
        super().__setattr__(name, value) 

    def __dir__(self):
        return super().__dir__() + list(self._values)




config = Configuracion({
    "host": "localhost",
    "puerto": 5432,
})

print(config.host)       # localhost
print(config.puerto)     # 5432
print("host" in dir(config))  # True
print(config.usuario) # AttributeError: No existe la configuración: usuario
config.host = '127.0.0.1'
