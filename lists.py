# Eliminar un elemento con "del"
print('Eliminar un elemento de una lista con "del"')
lista = ['bmw', 'audi', 'toyota', 'subaru']
print(lista)
del lista[1]
print(lista)

# Eliminar el ultimo elemento de una lista
print('Eliminar el ultimo elemento de una lista con "pop"')
lista = ['bmw', 'audi', 'toyota', 'subaru']
print(lista)
lista.pop()
print(lista)

# Eliminar un elemento de una lista con "pop" con el index
print('Eliminar un elemento de una lista con "pop(index)" con el index')
lista = ['bmw', 'audi', 'toyota', 'subaru']
print(lista)
lista.pop(2)
print(lista)

# Ordenar una lista con sort()
print('Ordenar una lista con sort()')
lista = ['bmw', 'audi', 'toyota', 'subaru']
print(lista)
lista.sort()
print(lista)

# Ordenar una lista con sort() en orden inverso alfabeticamente
# El metodo sort() modifica permanente e irreversible la lista
print('Ordenar una lista con sort() en orden inverso alfabeticamente')
lista = ['bmw', 'audi', 'toyota', 'subaru']
print(lista)
lista.sort(reverse=True)
print(lista)

# Ordenar alfabeticamente una lista temporalmente con la funcion sorted()
# El metodo sorted() no afecta el orden actual de la lista
# Tambien acepta el argumento reverse=True
# Ordenar una lista con sort()
print('Ordenar una lista temporalmente con la funcion sorted()')
lista = ['bmw', 'audi', 'toyota', 'subaru']
print(lista)
print(sorted(lista))
print(lista)

# Mostar una lista en orden inverso cronologicamente
# El metodo reverse() afecta permanentemente la lista, aunque si se le aplica de nuevo reverse() vuelve a la misma lista
print('Mostar una lista en orden inverso cronologicamente')
lista = ['bmw', 'audi', 'toyota', 'subaru']
print(lista)
lista.reverse()
print(lista)

# Usar range() para crear una lista de numeros
numbers = list(range(6))
print(numbers)
