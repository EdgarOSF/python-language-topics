m = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]
print(m)

print()

print('Get the first item of column 2')
col1 = [ row[1] for row in m ]
print(col1)

print()

print('Sum 1 to first item of each row')
col1 = [ row[0] + 1 for row in m ]
print(col1)

print()

print('Get first item of each row if is odd')
col1 = [ row[2] for row in m if row[2] % 2 == 0 ]
print(col1)

print()

print('Collet the number in diagonal')
col1 = [ m[i][i] for i in [0, 1, 2] ]
print(col1)

print()

print('Repeat characters in a string')
col1 = [ i * 2 for i in ['a', 'b', 'c'] ]
print(col1)

print()

print('Create a list with range')
print(list(range(4)))

print()

print('-6 to 2 by 2')
print(list(range(-6, 7, 2)))

print()

print('[[ n2, n3]]  from list [1, 2, 3, 4]')
col1 = [[n**2, n**3] for n in range(4)]
print(col1)

print()

print('Multiple values, "if" filters')
col1 = [[x, x // 2, x* 2] for x in range(-6, 7, 2) if x > 0]
print(col1)

print()

print('Make a generator of rows sums')
g = (sum(row) for row in m )
print(next(g))
print(next(g))
print(next(g))

print()

print('Make an unordered set of rows sums')
q = {sum(row) for row in m}
print(q)

print()

print('Make a key:value table of rows sums')
print({i: sum(m[i]) for i in range(len(m))})
print({i: sum(m[i]) for i in [0,1,2]})











