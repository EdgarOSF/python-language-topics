class RegistroDeComandos(type):

    registro = dict()
    
    def __new__(cls, name, bases, attrs):
        
        new_class = super().__new__(cls, name, bases, attrs)
        
        if new_class.__name__ != 'Comando':
            if 'nombre' not in attrs:
                raise ValueError('La clase no contiene el atributo nombre')
            
            nombre = attrs['nombre']

            if not isinstance(nombre, str):
                raise TypeError(f'El atributo {nombre!r} debe ser string')

            if nombre == '':
                raise ValueError(f'{nombre!r} no puede ser esta vacio')
            
            if nombre in cls.registro:
                raise ValueError(f'Ya existe un comando llamado {nombre!r}')
            
            
            RegistroDeComandos.registro[nombre] = new_class

        return new_class


class Comando(metaclass=RegistroDeComandos):
    pass 


class Saludar(Comando):
    nombre = 'saludar'

    def ejecutar(self):
        return 'Hola'


class Despedir(Comando):
    nombre = 'despedir'

    def ejecutar(self):
        return 'Adios'


print(RegistroDeComandos.registro)
print(RegistroDeComandos.registro["saludar"] is Saludar)  # True
print(RegistroDeComandos.registro["despedir"]().ejecutar())  # Adiós
