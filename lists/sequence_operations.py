l = [123, 'text', 1.23]
print(len(l))

print()

# Slicing a list return a new list
print(l[:-1])

print()

print('* Contat/repeat make a new list too.')
print(l + [4,5,6])

print()

print('* Can multiplay a list "l * 2"')
print(l * 2)

print()

print('Growing: add object at end of list')
l.append('Py')
print(l)

print()

print('Shrinking: delete an item in the middle')
l.pop(2)
print(l)

print()

print('* Sort a list')
m = ['bb', 'aa', 'cc']
print(m)
print('sorting...')
m.sort()
print(m)

print()

print('* Reversing a list.')
m.reverse()
print(m)
