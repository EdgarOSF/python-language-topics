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

# Copiar una lista
print('Copy a list')
my_foods = ['pizza', 'falafel', 'carrot cake']
friends_food = my_foods[:]
print(friends_food)

# Comprobar si un elemento esta en una lista
print('Comprobar si un elemento esta en una lista')
requested_toppings = ['mushrooms', 'onions', 'pineapple']
print('mushrooms' in requested_toppings)
print('pepperoni' in requested_toppings)
print('\n')
# Comprobar si un elemento no esta en una lista
print('Comprobar si un elemento esta en una lista')
banned_users = ['andrew', 'carolina', 'david']
user = 'marie'
print(user not in banned_users)
print(f"{user.title()}, you can post a response if you wish.")
print('\n')
