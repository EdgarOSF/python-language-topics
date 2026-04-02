D = dict(a=1, b=2, c=3, d=4)

print(D)

print()

print('keys()')
print(D.keys())

print()

print('values()')
print(D.values())

print()

print('items()')
print(D.items())

print()

print('Get an iterator from an iterable')
I = iter(D.keys())
print(next(I))
print(next(I))
print(next(I))

print()

print('Auto run the iteration protocol')
for key in D.keys():
    print(key, '=>', D[key])

print()

for key in D:
    print(key, '=>', D[key])

print()

for key, value in D.items():
    print(key, '=>', value)









