''' 
Cuando creamos una funcion dinamicamente python crea un objeto de funciona para nosotros
y este objeto de funcion tiene algunos valores que identifican a la funcion como, el nombre
de la funcion(sea anonima o no), docstring (si este se agrego), sus valores por defecto, su codigo
 y toda informacion global o no global que necesite para operar (closure.)
'''

 def f(x, ys=[123, 456]):
    '''
        adds x to each value in ys
    '''
    return [x + y for y in ys]

print(
        f'{f.__name__ = }',
        f'{f.__doc__ = }',
        f'{f.__code__ = }',
        f'{f.__code__.co_code = }',
        f'{f.__dafaults__ = }',
        f'{f.__closure__ = }',
        sep='\n',
    )
            

