list = ['uno', 'dos', 'tres']
list.remove('dos')
print(list)

# remover elemento en cualquie posicion
list2 = ['uno', 'dos', 'tres']
del list2[1]
print(list2)

# Eliminar el ultimo elemento de una lista
list3 = ['uno', 'dos', 'tres']
popped_list3 = list3.pop()
print(list3)
print(popped_list3)

# Eliminar elemento en cualquier posicion con pop()
list4 = ['uno', 'dos', 'tres']
popped_list4 = list4.pop(1)
print(list4)
print(popped_list4)

# Remover un elemento por su valor
print('#Remover un elemento por su valor')
list5 = ['uno', 'dos', 'tres']
print(list5)
list5.remove('tres')
print(list5)