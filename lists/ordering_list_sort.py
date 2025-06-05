# sort cambia el orden la lista permanentemente
list = ['nissan', 'toyota', 'bmw', 'subaru', 'audi']

list.sort()

print(list)

list.sort(reverse=True)
print(list)

# sorted no cambia el orden de la lista original
list2 = ['nissan', 'toyota', 'bmw', 'subaru', 'audi']

print('Esta es la lista original:', list2)

print('\nEsta es la lista ordenada: ', sorted(list2))

print('\nEs la lista original', list2)
