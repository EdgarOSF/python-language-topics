from collections import ChainMap


d1 = dict(a=1, b=2)
d2 = dict(a=2, b=4, c=6)


# Las instancias de ChainMap guardan referencias de listas que pueden ser buscadas como una.
# Al buscar un valor me devolvera el primer que encuentre en el orden en quelas listasfueron declaradas.
#

chain = ChainMap(d1, d2)

print(chain['a'])

print(chain['c'])

# Las actualizaciones y las inserciones solo afectan a la primera lista.
chain['c'] = -1
print(d1)
print(d2)
