D = {'a':1, 'b':2, 'c':3, 'd':4}
print('Use of the "in" test')
print('e' in D )

if not 'e' in D:
    print('Missin key!')

print()

print('Use the get method')

print(D.get('a', 'missing'))
print(D.get('e', 'missing'))

print()

print('if/else ternary expression form')
print(D['e'] if 'e' in D else 0)
